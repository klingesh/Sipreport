# -*- coding: utf-8 -*-
"""
Render the SIP report content into a Word document (.docx) and a Markdown
copy for quick review on GitHub.

    python3 tools/build_report.py

Outputs (relative to the repository root):
    Lingesh K - SIP Report 2026.docx
    SIP-Report-2026.md

If a scan of the internship certificate is placed at
assets/internship-certificate.jpg (or .png), it is embedded automatically on
the INTERNSHIP CERTIFICATE page; otherwise a placeholder box is inserted.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

from docx_writer import (Document, bookmark, drawing, esc, image_size,
                         page_break, para, rich, run, table, EMU_PER_INCH)
import report_content as rc

# Scan of the internship completion certificate, searched in this order.
CERT_CANDIDATES = ['assets/internship-certificate.jpg',
                   'assets/internship-certificate.jpeg',
                   'assets/internship-certificate.png',
                   'Internship Certificate.png',
                   'Internship Certificate.jpg']
# Title-page banner: Malaysia University of Science and Technology + ISSM.
LOGO_CANDIDATES = ['assets/issm-must-logo.jpg', 'assets/issm-must-logo.png']
BODY_LINE = 360           # 1.5 line spacing
DOC_TITLE = 'Summer Internship Project Report 2026 - Lingesh K'

# --- page geometry, used by the layout checker -----------------------------
PAGE_H_IN = 11.69                       # A4
TEXT_H_IN = PAGE_H_IN - 2.0             # 1" top and bottom margins
LINE_IN = {12: 0.2875, 13: 0.312, 14: 0.335, 16: 0.383, 20: 0.479}


# ---------------------------------------------------------------------------
# docx rendering
# ---------------------------------------------------------------------------
def _first_existing(names):
    for name in names:
        path = os.path.join(ROOT, name)
        if os.path.exists(path):
            return path
    return None


def find_certificate():
    return _first_existing(CERT_CANDIDATES)


def find_logo():
    return _first_existing(LOGO_CANDIDATES)


def logo_size_in(width_twips):
    """Logo scaled to the text width; returns (inches_w, inches_h)."""
    path = find_logo()
    if not path:
        return None
    px_w, px_h = image_size(path)
    w_in = width_twips / 1440.0
    return w_in, w_in * px_h / px_w


def logo_block(doc, sec, width):
    path = find_logo()
    if not path:
        return
    rel = doc.add_image(path)
    w_in, h_in = logo_size_in(width)
    sec.add(para(drawing(rel, int(w_in * EMU_PER_INCH), int(h_in * EMU_PER_INCH),
                         'MUST and ISSM Business School logo'),
                 jc='center', line=240, after=0))


def certificate_block(doc, sec, content_width_twips):
    """Embed the scanned certificate if available, else a placeholder box."""
    path = find_certificate()
    if path:
        rel = doc.add_image(path)
        px_w, px_h = image_size(path)
        max_w = int(content_width_twips / 1440 * EMU_PER_INCH)
        # heading block above the image uses ~1.4in, so cap the height to keep
        # the certificate on a single page
        max_h = int((TEXT_H_IN - 1.6) * EMU_PER_INCH)
        cx = max_w
        cy = int(cx * px_h / px_w)
        if cy > max_h:
            cy = max_h
            cx = int(cy * px_w / px_h)
        sec.add(para(drawing(rel, cx, cy, 'Internship Completion Certificate'),
                     jc='center', line=240, after=0))
        return
    note = ('[ Scanned copy of the Internship Completion Certificate issued by '
            'S. Ravi & Associates, Chartered Accountants, dated 17 July 2026, '
            'to be inserted here. ]')
    rows = [['\n' * 8 + note + '\n' * 8]]
    sec.add(table(rows, widths=[1], header=False, font_size=11,
                  page_width=content_width_twips))


def toc_table(width, estimates):
    """Table of contents whose page numbers are live Word cross-references."""
    rows = [['SL.NO', 'CHAPTER', 'PAGE NO.']]
    for ch in rc.CHAPTERS:
        n = ch['num']
        start, end = estimates.get(n, ('', ''))
        rows.append([
            str(n), ch['title'],
            f'{{{{PAGEREF ch{n}_start|{start}}}}} - '
            f'{{{{PAGEREF ch{n}_end|{end}}}}}'])
    return table(rows, widths=[1, 5, 2], page_width=width, align='center')


def render_blocks(doc, sec, blocks, width, chapter=None, estimates=None):
    for block in blocks:
        kind = block[0]
        payload = block[1] if len(block) > 1 else None

        if kind == 'big':
            sec.add(para(run(payload, bold=True, size=16), jc='center',
                         after=200, line=BODY_LINE))
        elif kind == 'cbold':
            sec.add(para(run(payload, bold=True), jc='center', after=40,
                         line=BODY_LINE))
        elif kind == 'center':
            sec.add(para(rich(payload), jc='center', after=40, line=BODY_LINE))
        elif kind == 'h1':
            sec.add(para(run(payload, bold=True, size=14), jc='center',
                         before=0, after=240, line=BODY_LINE, keep_next=True))
        elif kind == 'h2':
            sec.add(para(run(payload, bold=True, size=13), jc='left',
                         before=240, after=120, line=BODY_LINE, keep_next=True))
        elif kind == 'h3':
            sec.add(para(run(payload, bold=True, size=12), jc='left',
                         before=180, after=100, line=BODY_LINE, keep_next=True))
        elif kind == 'p':
            sec.add(para(rich(payload), jc='both', after=140, line=BODY_LINE))
        elif kind == 'bullets':
            justify = 'left' if (chapter and chapter.get('num') == 6) else 'both'
            for item in payload:
                sec.add(para(rich(item), jc=justify, num_id=1, after=80,
                             line=BODY_LINE))
            sec.add(para('', after=60, line=120))
        elif kind == 'table':
            rows = payload['rows']
            widths = payload.get('widths')
            sec.add(table(rows, widths=widths, page_width=width,
                          align='center' if payload.get('center') else 'left'))
            sec.add(para('', after=120, line=200))
        elif kind == 'gap':
            for _ in range(payload):
                sec.add(para('', after=0, line=BODY_LINE))
        elif kind == 'pagebreak':
            sec.add(page_break())
        elif kind == 'sign':
            left, right = payload
            sec.add(para(run(left, bold=False)
                         + ('<w:r><w:tab/></w:r>' if right else '')
                         + (run(right) if right else ''),
                         jc='left', after=140, line=BODY_LINE,
                         tabs=[('right', width)]))
        elif kind == 'box':
            sec.add(table([[payload]], widths=[1], header=False,
                          page_width=width))
        elif kind == 'certificate_image':
            certificate_block(doc, sec, width)
        elif kind == 'logo':
            logo_block(doc, sec, width)
        elif kind == 'toc':
            sec.add(toc_table(width, estimates or {}))
        else:
            raise ValueError(f'unknown block type: {kind}')


def divider_page(sec, chapter, bid):
    """Chapter divider page; carries the chapter's start bookmark."""
    mark = bookmark(f'ch{chapter["num"]}_start', bid)
    for i in range(8):
        sec.add(para(mark if i == 0 else '', after=0, line=BODY_LINE))
    title = chapter.get('divider_title')
    if title:
        sec.add(para(run(title, bold=True, size=20), jc='center', after=200,
                     line=BODY_LINE))
    else:
        sec.add(para(run(f'CHAPTER {chapter["num"]}', bold=True, size=20),
                     jc='center', after=200, line=BODY_LINE))
        sec.add(para(run(chapter['title'], bold=True, size=16), jc='center',
                     after=0, line=BODY_LINE))
    sec.add(page_break())


def build_docx(out_path):
    estimates = estimate_pages()
    doc = Document(a4=True, margins=(1440, 1440, 1440, 1800), title=DOC_TITLE)
    width = doc.content_width

    front = doc.section()
    render_blocks(doc, front, rc.FRONT, width, estimates=estimates)

    bid = 100
    for i, chapter in enumerate(rc.CHAPTERS):
        sec = doc.section(header_left=chapter['header'],
                          header_right=['SUMMER INTERNSHIP', 'PROJECT'],
                          page_numbers=True,
                          restart_at=1 if i == 0 else None)
        divider_page(sec, chapter, bid)
        bid += 1
        render_blocks(doc, sec, chapter['blocks'], width, chapter, estimates)
        # end-of-chapter bookmark, so the TOC can show a page range
        sec.add(para(bookmark(f'ch{chapter["num"]}_end', bid), after=0,
                     line=240))
        bid += 1

    doc.save(out_path)
    return out_path


# ---------------------------------------------------------------------------
# markdown rendering (for reviewing the text on GitHub)
# ---------------------------------------------------------------------------
def md_blocks(blocks, out):
    for block in blocks:
        kind = block[0]
        payload = block[1] if len(block) > 1 else None
        if kind in ('big', 'h1'):
            out.append(f'\n## {payload}\n')
        elif kind == 'h2':
            out.append(f'\n### {payload}\n')
        elif kind == 'h3':
            out.append(f'\n#### {payload}\n')
        elif kind in ('p', 'center'):
            out.append(payload + '\n')
        elif kind == 'cbold':
            out.append(f'**{payload}**\n')
        elif kind == 'bullets':
            for item in payload:
                out.append(f'- {item}')
            out.append('')
        elif kind == 'table':
            rows = payload['rows']
            out.append('| ' + ' | '.join(rows[0]) + ' |')
            out.append('|' + '---|' * len(rows[0]))
            for row in rows[1:]:
                out.append('| ' + ' | '.join(
                    c.replace('\n', ' ') for c in row) + ' |')
            out.append('')
        elif kind == 'sign':
            left, right = payload
            out.append(f'{left}  {right}'.strip() + '\n')
        elif kind == 'box':
            out.append(f'> {payload}\n')
        elif kind == 'certificate_image':
            path = find_certificate()
            if path:
                rel = os.path.relpath(path, ROOT)
                out.append(f'![Internship Completion Certificate]({rel})\n')
            else:
                out.append('> [ Scanned copy of the Internship Completion '
                           'Certificate to be inserted here. ]\n')
        elif kind == 'logo':
            path = find_logo()
            if path:
                rel = os.path.relpath(path, ROOT)
                out.append(f'![Malaysia University of Science and Technology '
                           f'and ISSM Business School]({rel})\n')
        elif kind == 'pagebreak':
            out.append('\n---\n')


def build_md(out_path):
    # No summary block of personal details here: the report text below starts
    # at the title page, exactly as in the .docx.
    out = ['> Markdown copy of the report text, generated from '
           '`tools/report_content.py` for easy reading. The submission copy is '
           'the .docx file.',
           '']
    md_blocks(rc.FRONT, out)
    for chapter in rc.CHAPTERS:
        out.append('\n---\n')
        out.append(f'# CHAPTER {chapter["num"]} — {chapter["title"]}\n')
        md_blocks(chapter['blocks'], out)
    text = '\n'.join(out)
    text = re.sub(r'\n{4,}', '\n\n\n', text)
    with open(out_path, 'w', encoding='utf-8') as fh:
        fh.write(text + '\n')
    return out_path


# ---------------------------------------------------------------------------
CHARS_PER_LINE = 96          # Times New Roman 12pt across ~6" of A4
TEXT_WIDTH_TWIPS = 8666      # A4 minus 1" + 1.25" margins


def _wrapped(text, chars_per_line):
    """Lines a string occupies, allowing for words that cannot be split."""
    import math
    return max(1, math.ceil(len(text) / chars_per_line))


def _height(block, width=TEXT_WIDTH_TWIPS):
    """Vertical space a single block occupies, in inches."""
    kind = block[0]
    payload = block[1] if len(block) > 1 else None
    body = LINE_IN[12]
    if kind in ('p', 'center'):
        return _wrapped(payload, CHARS_PER_LINE) * body + 140 / 1440
    if kind == 'cbold':
        return body + 40 / 1440
    if kind == 'big':
        return LINE_IN[16] + 200 / 1440
    if kind == 'h1':
        return LINE_IN[14] + 240 / 1440
    if kind == 'h2':
        return LINE_IN[13] + (240 + 120) / 1440
    if kind == 'h3':
        return _wrapped(payload, CHARS_PER_LINE) * body + (180 + 100) / 1440
    if kind == 'bullets':
        total = 0.0
        for item in payload:
            total += _wrapped(item, CHARS_PER_LINE - 8) * body + 80 / 1440
        return total + 60 / 1440 + body
    if kind == 'table':
        rows, widths = payload['rows'], payload.get('widths')
        widths = widths or [1] * len(rows[0])
        share = sum(widths)
        total = 0.0
        for row in rows:
            cell_lines = [
                _wrapped(c, max(10, int(CHARS_PER_LINE * 1.18
                                        * widths[i] / share)))
                for i, c in enumerate(row)]
            total += max(cell_lines) * 0.19 + 40 / 1440      # 11pt, single
        return total + 0.25 + body
    if kind == 'gap':
        return payload * body
    if kind == 'toc':
        return _height(('table', {'rows': [['x'] * 3] * 7, 'widths': [1, 5, 2]}))
    if kind == 'sign':
        return body + 140 / 1440
    if kind == 'certificate_image':
        path = find_certificate()
        if not path:
            return TEXT_H_IN - 2.0
        px_w, px_h = image_size(path)
        w_in = width / 1440.0
        return min(w_in * px_h / px_w, TEXT_H_IN - 1.6)
    if kind == 'logo':
        size = logo_size_in(width)
        return size[1] if size else 0.0
    if kind in ('pagebreak', 'box'):
        return 0.0
    return 0.0


def check_front_pages(verbose=True):
    """Front matter is one page per page-break: flag any page that overflows."""
    import math
    pages, current, used = [], [], 0.0
    for block in rc.FRONT:
        if block[0] == 'pagebreak':
            pages.append((used, current))
            current, used = [], 0.0
            continue
        used += _height(block)
        current.append(block[0])
    pages.append((used, current))

    # (label, pages the section is meant to occupy)
    expected = [('title page', 1), ('certificate', 1),
                ('internship certificate', 1), ('declaration', 1),
                ('acknowledgement', 1), ('executive summary', 2),
                ('table of contents', 1)]
    problems = []
    if verbose:
        print(f'front matter layout (A4 text height {TEXT_H_IN:.2f}in):')
    for i, (used, _kinds) in enumerate(pages):
        name, allow = expected[i] if i < len(expected) else (f'page {i + 1}', 1)
        needed = max(1, math.ceil(used / TEXT_H_IN))
        fill_last = (used - (needed - 1) * TEXT_H_IN) / TEXT_H_IN * 100
        note = f'{needed} page' + ('s' if needed > 1 else '')
        if needed > allow:
            note += '  <-- SPILLS past its intended length'
            problems.append(name)
        elif needed > 1 and fill_last < 15:
            note += '  <-- leaves an almost empty last page'
            problems.append(name)
        elif used > TEXT_H_IN - 0.35 and needed == 1:
            note += '  <-- very tight, check in Word'
            problems.append(name)
        if verbose:
            print(f'  {name:<26}{used:>6.2f}in   {note}'
                  f'{"" if needed > 1 else f"  ({fill_last:.0f}% of the page)"}')
    return problems


def estimate_pages(verbose=False):
    """Return {chapter_no: (start_page, end_page)} for the TOC fallback text."""
    import math
    page = 1
    out = {}
    rows = []
    for ch in rc.CHAPTERS:
        inches = sum(_height(b) for b in ch['blocks'])
        body = max(1, math.ceil(inches / TEXT_H_IN))
        pages = body + 1                      # + divider page
        out[ch['num']] = (page, page + pages - 1)
        rows.append((ch['num'], ch['title'], pages, page, page + pages - 1))
        page += pages
    if verbose:
        front = len([b for b in rc.FRONT if b[0] == 'pagebreak']) + 1
        print(f'front matter: {front} pages (unnumbered)')
        for n, title, pages, start, end in rows:
            print(f'  CH{n} {title[:30]:<32} {pages:>3} pages   {start}-{end}')
        print(f'  numbered pages: {page - 1}   total: {front + page - 1}')
    return out


if __name__ == '__main__':
    docx_path = build_docx(os.path.join(ROOT, 'Lingesh K - SIP Report 2026.docx'))
    md_path = build_md(os.path.join(ROOT, 'SIP-Report-2026.md'))
    print('wrote', os.path.relpath(docx_path, ROOT))
    print('wrote', os.path.relpath(md_path, ROOT))
    print()
    estimate_pages(verbose=True)
    print()
    issues = check_front_pages()
    print()
    cert, logo = find_certificate(), find_logo()
    print(f'certificate scan : {os.path.relpath(cert, ROOT) if cert else "MISSING"}')
    print(f'title page logo  : {os.path.relpath(logo, ROOT) if logo else "MISSING"}')
    if issues:
        print(f'\nreview these pages: {", ".join(issues)}')
