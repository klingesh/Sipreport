# -*- coding: utf-8 -*-
"""
Structural check of the generated .docx: parses every part, verifies that the
relationships and bookmark cross-references resolve, and prints the extracted
text so the content can be eyeballed.

    python3 tools/verify_docx.py "Lingesh K - SIP Report 2026.docx" [--text]
"""
import re
import sys
import xml.dom.minidom as minidom
import zipfile

W = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'


def text_of(xml_bytes):
    dom = minidom.parseString(xml_bytes)
    out = []
    for node in dom.getElementsByTagNameNS(W, 'p'):
        buf = []
        for t in node.getElementsByTagNameNS(W, 't'):
            if t.firstChild:
                buf.append(t.firstChild.nodeValue or '')
        for _ in node.getElementsByTagNameNS(W, 'tab'):
            buf.append(' ')
        line = ''.join(buf).strip()
        if line:
            out.append(line)
    return out


def main(path, dump_text=False):
    problems = []
    with zipfile.ZipFile(path) as z:
        names = z.namelist()
        parts = {}
        for n in names:
            if n.endswith('.xml') or n.endswith('.rels'):
                try:
                    minidom.parseString(z.read(n))
                except Exception as exc:                 # noqa: BLE001
                    problems.append(f'{n}: malformed XML -> {exc}')
                parts[n] = z.read(n).decode('utf-8', 'replace')

        doc = parts['word/document.xml']
        rels = parts['word/_rels/document.xml.rels']

        # every r:id used in the document must exist in the rels part
        used = set(re.findall(r'r:(?:id|embed)="([^"]+)"', doc))
        declared = set(re.findall(r'Id="([^"]+)"', rels))
        missing = used - declared
        if missing:
            problems.append(f'relationship ids used but not declared: {missing}')

        # every part referenced from rels must exist in the package
        for target in re.findall(r'Target="([^"]+)"', rels):
            if target.startswith('http'):
                continue
            if f'word/{target}' not in names:
                problems.append(f'rels points at missing part: word/{target}')

        # bookmarks referenced by PAGEREF fields must exist
        refs = set(re.findall(r'PAGEREF (\w+)', doc))
        marks = set(re.findall(r'w:bookmarkStart[^>]*w:name="([^"]+)"', doc))
        if refs - marks:
            problems.append(f'PAGEREF without bookmark: {sorted(refs - marks)}')

        # unsubstituted template tokens
        if '{{' in doc:
            problems.append('unsubstituted {{...}} token left in document')

        sections = doc.count('<w:sectPr>')
        headers = [n for n in names if re.match(r'word/header\d+\.xml', n)]
        images = [n for n in names if n.startswith('word/media/')]
        page_fields = len(re.findall(r'instr=" PAGE', doc))
        tables = doc.count('<w:tbl>')
        paras = doc.count('<w:p>')
        bullets = doc.count('<w:numId w:val="1"/>')

        lines = text_of(z.read('word/document.xml'))
        words = sum(len(l.split()) for l in lines)

    print(f'file            : {path}')
    print(f'parts           : {len(names)}')
    print(f'sections        : {sections}   headers: {len(headers)}')
    print(f'paragraphs      : {paras}   tables: {tables}   bullets: {bullets}')
    print(f'PAGE fields     : {page_fields}   '
          f'PAGEREF fields: {len(re.findall(r"PAGEREF", doc))}')
    print(f'bookmarks       : {len(marks)} -> {", ".join(sorted(marks))}')
    print(f'embedded images : {len(images)}')
    print(f'text lines      : {len(lines)}   words: {words}')
    print()
    if problems:
        print('PROBLEMS:')
        for p in problems:
            print('  -', p)
        return 1
    print('OK: package structure, relationships and cross-references all valid')
    if dump_text:
        print('\n' + '=' * 70)
        print('\n'.join(lines))
    return 0


if __name__ == '__main__':
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    sys.exit(main(args[0], '--text' in sys.argv))
