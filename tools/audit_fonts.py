# -*- coding: utf-8 -*-
"""
Audit the typography of a generated report against the sample report's
measured specification.

    python3 tools/audit_fonts.py "Report.docx"

The expected values were measured directly from Final SIP KYR.pdf by reading
the Tf operators and font descriptors of each text run.
"""
import re
import sys
import xml.dom.minidom as minidom
import zipfile

W = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'

# element -> (points, bold, italic) as measured in the sample report
SPEC = [
    ('title page heading', 16, True, False),
    ('submitted-to paragraph', 14, True, True),
    ('degree line', 14, True, False),
    ('SUBMITTED BY', 12, False, False),
    ('student name', 12, True, False),
    ('register number', 12, False, False),
    ('college name', 14, True, False),
    ('city', 14, True, False),
    ('CERTIFICATE heading', 14, True, False),
    ('INTERNSHIP CERTIFICATE heading', 26, True, False),
    ('DECLARATION heading', 14, True, False),
    ('ACKNOWLEDGEMENT heading', 14, True, False),
    ('executive summary heading', 12, True, False),
    ('TABLE OF CONTENTS heading', 14, True, False),
    ('table of contents cells', 14, True, False),
    ('chapter divider lines', 16, True, False),
    ('chapter title in body', 14, True, False),
    ('section heading (n.n)', 14, True, False),
    ('sub-section heading (n.n.n)', 12, True, False),
    ('body text', 12, False, False),
    ('bullet body text', 12, False, False),
    ('content table body text', 12, False, False),
    ('running header', 12, True, False),
    ('running footer', 12, False, False),
]


def runs(xml):
    """(text, size_pt, bold, italic) for every run that carries text."""
    out = []
    dom = minidom.parseString(xml)
    for r in dom.getElementsByTagNameNS(W, 'r'):
        out.extend(_run_info(r))
    return out


def _run_info(r):
    text = ''.join(t.firstChild.nodeValue
                   for t in r.getElementsByTagNameNS(W, 't')
                   if t.firstChild)
    if not text.strip():
        return []
    sz = r.getElementsByTagNameNS(W, 'sz')
    size = int(sz[0].getAttribute('w:val')) / 2 if sz else 12.0
    return [(text, size, bool(r.getElementsByTagNameNS(W, 'b')),
             bool(r.getElementsByTagNameNS(W, 'i')))]


def first_bullet_run(xml):
    """First run of the first bulleted paragraph (numPr present)."""
    dom = minidom.parseString(xml)
    for p in dom.getElementsByTagNameNS(W, 'p'):
        if not p.getElementsByTagNameNS(W, 'numPr'):
            continue
        infos = [i for r in p.getElementsByTagNameNS(W, 'r')
                 for i in _run_info(r)]
        if infos:
            longest = max(infos, key=lambda i: len(i[0]))
            return longest[1:]
    return None


def first_table_body_run(xml):
    """Longest run in a body row of the first content table.

    The table of contents is skipped: its cells are deliberately 14 pt bold,
    matching the sample report."""
    dom = minidom.parseString(xml)
    for tbl in list(dom.getElementsByTagNameNS(W, 'tbl'))[1:]:
        rows = tbl.getElementsByTagNameNS(W, 'tr')
        for row in rows[1:]:                     # skip the header row
            infos = [i for r in row.getElementsByTagNameNS(W, 'r')
                     for i in _run_info(r)]
            if infos:
                return max(infos, key=lambda i: len(i[0]))[1:]
    return None


def main(path):
    with zipfile.ZipFile(path) as z:
        raw = z.read('word/document.xml')
        doc = runs(raw)
        hdr = runs(z.read('word/header3.xml'))
        ftr = runs(z.read('word/footer3.xml'))
        bullet = first_bullet_run(raw)
        cell = first_table_body_run(raw)

    def find(pred):
        for t, s, b, i in doc:
            if pred(t):
                return s, b, i
        return None

    found = {
        'title page heading': find(lambda t: t.startswith('SUMMER INTERNSHIP PROJECT (SIP)')),
        'submitted-to paragraph': find(lambda t: t.startswith('Summer Internship Project Report submitted')),
        'degree line': find(lambda t: t == 'MASTER OF BUSINESS ADMINISTRATION'),
        'SUBMITTED BY': find(lambda t: t == 'SUBMITTED BY'),
        'student name': find(lambda t: re.fullmatch(r'[A-Z][A-Z .]+[A-Z.]', t) is not None
                             and 'SUMMER' not in t and 'MASTER' not in t
                             and 'SUBMITTED' not in t and len(t) > 8),
        'register number': find(lambda t: re.fullmatch(r'OSI\d+', t) is not None),
        'college name': find(lambda t: t == 'Indian School of Science and Management'),
        'city': find(lambda t: t == 'Chennai'),
        'CERTIFICATE heading': find(lambda t: t == 'CERTIFICATE'),
        'INTERNSHIP CERTIFICATE heading': find(lambda t: t == 'INTERNSHIP CERTIFICATE'),
        'DECLARATION heading': find(lambda t: t == 'DECLARATION'),
        'ACKNOWLEDGEMENT heading': find(lambda t: t == 'ACKNOWLEDGEMENT'),
        'executive summary heading': find(lambda t: t == 'The Executive Summary'),
        'TABLE OF CONTENTS heading': find(lambda t: t == 'TABLE OF CONTENTS'),
        'table of contents cells': find(lambda t: t == 'SL.NO'),
        'chapter divider lines': find(lambda t: t.startswith('CHAPTER  ')),
        'chapter title in body': find(lambda t: t.startswith('1. INDUSTRY AND COMPANY')),
        'section heading (n.n)': find(lambda t: re.match(r'^1\.1\s\s', t) is not None),
        'sub-section heading (n.n.n)': find(lambda t: re.match(r'^1\.3\.1\s\s', t) is not None),
        'body text': find(lambda t: len(t) > 200),
        'bullet body text': bullet,
        'content table body text': cell,
        'running header': (hdr[0][1], hdr[0][2], hdr[0][3]) if hdr else None,
        'running footer': (ftr[0][1], ftr[0][2], ftr[0][3]) if ftr else None,
    }

    print(f'{path}\n')
    print(f'{"element":<32}{"expected":<22}{"in this report":<22}result')
    print('-' * 88)
    ok = bad = 0
    for name, pt, bold, italic in SPEC:
        got = found.get(name)
        want = f'{pt}pt' + (' bold' if bold else '') + (' italic' if italic else '')
        if got is None:
            print(f'{name:<32}{want:<22}{"not found":<22}--')
            continue
        g_pt, g_b, g_i = got
        have = (f'{g_pt:g}pt' + (' bold' if g_b else '')
                + (' italic' if g_i else ''))
        match = (abs(g_pt - pt) < 0.01 and g_b == bold and g_i == italic)
        print(f'{name:<32}{want:<22}{have:<22}{"ok" if match else "MISMATCH"}')
        ok, bad = ok + match, bad + (not match)
    print('-' * 88)
    print(f'{ok} match, {bad} mismatch')
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
