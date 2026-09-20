# -*- coding: utf-8 -*-
"""
Compare the formatting and structure of two generated reports.

    python3 tools/compare_docx.py "A.docx" "B.docx"

Text content is expected to differ (different students, different companies).
What must match is everything else: page geometry, fonts, spacing, running
header and footer construction, front matter sequence, chapter scaffolding,
table of contents mechanics and heading levels.
"""
import re
import sys
import xml.dom.minidom as minidom
import zipfile

W = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'


def load(path):
    with zipfile.ZipFile(path) as z:
        return {n: z.read(n).decode('utf-8', 'replace') for n in z.namelist()
                if n.endswith('.xml') or n.endswith('.rels')}, z.namelist()


def paragraphs(xml):
    """(text, properties-xml) for every paragraph, in document order."""
    out = []
    dom = minidom.parseString(xml)
    for p in dom.getElementsByTagNameNS(W, 'p'):
        text = ''.join(t.firstChild.nodeValue
                       for t in p.getElementsByTagNameNS(W, 't')
                       if t.firstChild)
        ppr = p.getElementsByTagNameNS(W, 'pPr')
        sizes = [s.getAttribute('w:val')
                 for s in p.getElementsByTagNameNS(W, 'sz')]
        bold = bool(p.getElementsByTagNameNS(W, 'b'))
        italic = bool(p.getElementsByTagNameNS(W, 'i'))
        jc = p.getElementsByTagNameNS(W, 'jc')
        out.append({
            'text': text.strip(),
            'size': sizes[0] if sizes else None,
            'bold': bold,
            'italic': italic,
            'jc': jc[0].getAttribute('w:val') if jc else None,
            'xml': ppr[0].toxml() if ppr else '',
        })
    return out


def fingerprint(path):
    parts, names = load(path)
    doc = parts['word/document.xml']
    paras = paragraphs(doc)
    fp = {}

    # --- package ---
    fp['sections'] = doc.count('<w:sectPr>')
    fp['header parts'] = len([n for n in names if re.match(r'word/header\d', n)])
    fp['footer parts'] = len([n for n in names if re.match(r'word/footer\d', n)])
    fp['numbering part'] = 'word/numbering.xml' in names
    fp['images'] = len([n for n in names if n.startswith('word/media/')])

    # --- page geometry ---
    m = re.search(r'<w:pgSz w:w="(\d+)" w:h="(\d+)"/>', doc)
    fp['page size (twips)'] = f'{m.group(1)} x {m.group(2)}' if m else None
    m = re.search(r'<w:pgMar w:top="(\d+)" w:right="(\d+)" w:bottom="(\d+)" '
                  r'w:left="(\d+)"', doc)
    fp['margins t/r/b/l'] = ' / '.join(m.groups()) if m else None
    fp['numbering restarts at'] = (re.search(r'pgNumType w:start="(\d+)"', doc)
                                   or [None, '-'])[1]

    # --- defaults from styles.xml / settings.xml ---
    st = parts['word/styles.xml']
    m = re.search(r'<w:rFonts w:ascii="([^"]+)"', st)
    fp['body font'] = m.group(1) if m else None
    m = re.search(r'<w:sz w:val="(\d+)"/>', st)
    fp['body size (half-pt)'] = m.group(1) if m else None
    m = re.search(r'<w:spacing w:after="(\d+)" w:line="(\d+)"', st)
    fp['default spacing after/line'] = f'{m.group(1)} / {m.group(2)}' if m else None
    m = re.search(r'<w:jc w:val="(\w+)"/>', st)
    fp['default alignment'] = m.group(1) if m else None
    fp['fields auto-update'] = 'updateFields' in parts['word/settings.xml']

    # --- running header construction ---
    hdr = parts.get('word/header3.xml', '')
    fp['header lines'] = hdr.count('<w:p>')
    fp['header left text'] = re.findall(r'<w:t[^>]*>([^<]*)</w:t>', hdr)[:1]
    fp['header bold size'] = (re.search(r'<w:sz w:val="(\d+)"', hdr)
                              or [None, None])[1]
    m = re.search(r'<w:bottom w:val="single" w:sz="(\d+)"[^>]*w:color="(\w+)"',
                  hdr)
    fp['header rule (size/colour)'] = f'{m.group(1)} / {m.group(2)}' if m else None

    # --- running footer construction ---
    ftr = parts.get('word/footer3.xml', '')
    fp['footer text'] = re.findall(r'<w:t[^>]*>([^<]*)</w:t>', ftr)[:1]
    fp['footer page field'] = 'instr=" PAGE' in ftr
    m = re.search(r'<w:top w:val="single" w:sz="(\d+)"[^>]*w:color="(\w+)"', ftr)
    fp['footer rule (size/colour)'] = f'{m.group(1)} / {m.group(2)}' if m else None

    # --- front matter sequence: the big centred headings ---
    front = []
    for p in paras:
        if p['size'] == '28' and p['jc'] == 'center' and p['text']:
            front.append(p['text'])
        if p['text'].startswith('1. '):
            break
    fp['front matter headings'] = front

    # --- title page run styles ---
    title_page = paras[:24]
    fp['title page: bold-italic line'] = any(
        p['bold'] and p['italic'] for p in title_page)
    fp['title page: plain SUBMITTED BY'] = any(
        p['text'] == 'SUBMITTED BY' and not p['bold'] for p in title_page)

    # --- chapter scaffolding ---
    dividers = [p['text'] for p in paras
                if re.fullmatch(r'CHAPTER\s+\d|REFERENCES', p['text'] or '')
                and p['size'] == '28']
    fp['divider pages'] = dividers
    h1 = [p['text'] for p in paras
          if p['size'] == '28' and p['jc'] == 'center'
          and re.match(r'^\d\.\s|^REFERENCES$', p['text'] or '')]
    fp['chapter title lines'] = h1
    h2 = [p['text'].split()[0] for p in paras
          if p['size'] == '26' and re.match(r'^\d\.\d', p['text'] or '')]
    fp['section numbers'] = h2
    fp['sub-section count'] = len([p for p in paras if p['size'] == '24'
                                   and p['bold']
                                   and re.match(r'^\d\.\d\.\d|^Week ',
                                                p['text'] or '')])

    # --- body text formatting ---
    body = [p for p in paras if p['jc'] == 'both' and len(p['text']) > 120]
    fp['justified body paragraphs'] = len(body)
    fp['body line spacing'] = (re.search(r'w:line="(\d+)"', body[0]['xml'])
                               or [None, None])[1] if body else None
    fp['first-line indents'] = doc.count('w:firstLine="720"')

    # --- tables, fields, bookmarks ---
    fp['tables'] = doc.count('<w:tbl>')
    fp['toc row height'] = (re.search(r'w:trHeight w:val="(\d+)"', doc)
                            or [None, None])[1]
    fp['PAGEREF fields'] = len(re.findall(r'PAGEREF', doc))
    fp['bookmarks'] = len(re.findall(r'w:bookmarkStart', doc))
    fp['bullet list items'] = doc.count('<w:numId w:val="1"/>')
    m = re.search(r'wp:extent cx="(\d+)" cy="(\d+)"', doc)
    fp['logo size (EMU)'] = f'{m.group(1)} x {m.group(2)}' if m else 'none'
    return fp


def main(path_a, path_b):
    a, b = fingerprint(path_a), fingerprint(path_b)
    name_a = path_a.split('/')[-1].replace('.docx', '')
    name_b = path_b.split('/')[-1].replace('.docx', '')

    # items where the two reports are expected to differ in content, not form
    content_keys = {'front matter headings', 'header left text'}

    print(f'A = {name_a}')
    print(f'B = {name_b}\n')
    print(f'{"":36}{"A":<34}{"B":<34}')
    print('-' * 104)
    same = diff = 0
    notes = []
    for key in a:
        va, vb = a[key], b[key]
        sa, sb = str(va), str(vb)
        equal = sa == sb
        if key in content_keys and not equal:
            # compare shape rather than the words
            equal = len(va) == len(vb)
            if equal:
                notes.append(key)
        mark = '  ok ' if equal else ' DIFF'
        if equal:
            same += 1
        else:
            diff += 1
        print(f'{mark} {key:<30}{sa[:32]:<34}{sb[:32]:<34}')
    print('-' * 104)
    print(f'{same} identical, {diff} different')
    if notes:
        print('\nmatched on structure, wording differs as expected: '
              + ', '.join(notes))
    return 0 if diff == 0 else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1], sys.argv[2]))
