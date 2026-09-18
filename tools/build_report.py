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
BODY_LINE = 360           # 1.5 line spacing
DOC_TITLE = 'Summer Internship Project Report 2026 - Lingesh K'


# ---------------------------------------------------------------------------
# docx rendering
# ---------------------------------------------------------------------------
def find_certificate():
    for name in CERT_CANDIDATES:
        path = os.path.join(ROOT, name)
        if os.path.exists(path):
            return path
    return None


def certificate_block(doc, sec, content_width_twips):
    """Embed the scanned certificate if available, else a placeholder box."""
    path = find_certificate()
    if path:
        rel = doc.add_image(path)
        px_w, px_h = image_size(path)
        max_w = int(content_width_twips / 1440 * EMU_PER_INCH)
        max_h = int(8.2 * EMU_PER_INCH)          # leave room for the heading
        cx = max_w
        cy = int(cx * px_h / px_w)
        if cy > max_h:
            cy = max_h
            cx = int(cy * px_w / px_h)
        sec.add(para(drawing(rel, cx, cy, 'Internship Completion Certificate'),
                     jc='center', line=240, after=0))
        return
    note = ('[  Scanned copy of the Internship Completion Certificate issued by '
            'S. Ravi & Associates, Chartered Accountants, dated 17 July 2026, '
            'to be inserted here.  ]')
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
                          header_right='SUMMER INTERNSHIP PROJECT',
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
        elif kind == 'pagebreak':
            out.append('\n---\n')


def build_md(out_path):
    out = [f'# Summer Internship Project (SIP) – 2026',
           '',
           f'**{rc.STUDENT}** ({rc.REG_NO}) · MBA (Finance) · '
           'Indian School of Science and Management, Chennai',
           '',
           f'Internship: {rc.FIRM}, Mylapore, Chennai · '
           f'{rc.PERIOD} · Guide: {rc.MENTOR}, {rc.MENTOR_ROLE}',
           '',
           '> Markdown copy of the report text, generated from '
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
LINES_PER_PAGE = 31          # 1.5 line spacing, 1" top/bottom margins


def _lines(blocks):
    """Estimate how many text lines a list of blocks occupies."""
    import math
    total = 0.0
    for b in blocks:
        kind = b[0]
        payload = b[1] if len(b) > 1 else None
        if kind in ('p', 'center'):
            total += math.ceil(len(payload) / CHARS_PER_LINE) + 0.4
        elif kind in ('cbold',):
            total += 1.2
        elif kind == 'big':
            total += 2.2
        elif kind == 'h1':
            total += 2.4
        elif kind == 'h2':
            total += 2.2
        elif kind == 'h3':
            total += 2.0
        elif kind == 'bullets':
            for item in payload:
                total += math.ceil(len(item) / (CHARS_PER_LINE - 8)) + 0.35
            total += 0.5
        elif kind == 'table':
            for row in payload['rows']:
                widths = payload.get('widths') or [1] * len(row)
                share = sum(widths)
                cell_lines = [
                    math.ceil(len(c) / max(12, CHARS_PER_LINE * 1.15
                                           * widths[i] / share))
                    for i, c in enumerate(row)]
                total += max(cell_lines) * 0.75 + 0.3
            total += 1.0
        elif kind == 'gap':
            total += payload
        elif kind == 'toc':
            total += 10
        elif kind == 'certificate_image':
            total += LINES_PER_PAGE - 6
        elif kind == 'pagebreak':
            total = math.ceil(total / LINES_PER_PAGE) * LINES_PER_PAGE
    return total


def estimate_pages(verbose=False):
    """Return {chapter_no: (start_page, end_page)} for the TOC fallback text."""
    import math
    page = 1
    out = {}
    rows = []
    for ch in rc.CHAPTERS:
        body = math.ceil(_lines(ch['blocks']) / LINES_PER_PAGE)
        pages = body + 1                      # + divider page
        out[ch['num']] = (page, page + pages - 1)
        rows.append((ch['num'], ch['title'], pages, page, page + pages - 1))
        page += pages
    if verbose:
        front = math.ceil(_lines(rc.FRONT) / LINES_PER_PAGE)
        print(f'front matter: ~{front} pages (unnumbered)')
        for n, title, pages, start, end in rows:
            print(f'  CH{n} {title[:30]:<32} {pages:>3} pages   {start}-{end}')
        print(f'  numbered pages: {page - 1}   total: ~{front + page - 1}')
    return out


if __name__ == '__main__':
    docx_path = build_docx(os.path.join(ROOT, 'Lingesh K - SIP Report 2026.docx'))
    md_path = build_md(os.path.join(ROOT, 'SIP-Report-2026.md'))
    print('wrote', os.path.relpath(docx_path, ROOT))
    print('wrote', os.path.relpath(md_path, ROOT))
    print()
    estimate_pages(verbose=True)
