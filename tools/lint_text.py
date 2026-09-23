# -*- coding: utf-8 -*-
"""
Proof-reading pass over the report content: catches the small typographic
faults that show up in a printed, justified document.

    python3 tools/lint_text.py                 # checks every report
    python3 tools/lint_text.py report_content  # checks one content module
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import importlib

rc = None          # content module being checked

CHECKS = [
    (r'  +', 'double space'),
    (r'\s+[,.;:]', 'space before punctuation'),
    (r'[,;:][^\s\d)]', 'missing space after punctuation'),
    (r'\.\.', 'double full stop'),
    (r"(?<![\ws])'(?![\ws])", 'stray straight apostrophe'),
    (r'\s-\s', 'hyphen used as a dash (use an en dash)'),
    (r'\bthe the\b|\band and\b|\bof of\b|\bto to\b|\bin in\b|\bis is\b',
     'repeated word'),
    (r'\bteh\b|\brecieve\b|\bseperate\b|\boccured\b|\bacommodate\b',
     'common misspelling'),
    (r'[A-Za-z]\(', 'missing space before bracket'),
    (r'\s\)', 'space before closing bracket'),
]


def iter_text():
    def walk(blocks, where):
        for b in blocks:
            kind = b[0]
            payload = b[1] if len(b) > 1 else None
            if kind in ('p', 'center', 'cbold', 'big', 'h1', 'h2', 'h3'):
                yield where, kind, payload
            elif kind == 'bullets':
                for item in payload:
                    yield where, 'bullet', item
            elif kind == 'table':
                for row in payload['rows']:
                    for cell in row:
                        yield where, 'cell', cell
            elif kind == 'sign':
                for part in payload:
                    if part:
                        yield where, 'sign', part

    yield from walk(rc.FRONT, 'front matter')
    for ch in rc.CHAPTERS:
        yield from walk(ch['blocks'], f'chapter {ch["num"]}')


def main():
    findings = []
    sentences = 0
    words = 0
    for where, kind, text in iter_text():
        words += len(text.split())
        sentences += len(re.findall(r'[.!?](?:\s|$)', text))
        probe = re.sub(r'https?://\S+', 'URL', text)      # URLs are not prose
        probe = probe.replace('**', '')
        for pattern, label in CHECKS:
            # headings deliberately use "1.1  TITLE" with a double space
            if label == 'double space' and kind in ('h1', 'h2', 'h3'):
                continue
            for m in re.finditer(pattern, probe):
                snippet = probe[max(0, m.start() - 35):m.end() + 35]
                findings.append((where, kind, label, snippet.strip()))
        # sentences that run very long are hard to read when justified
        for part in re.split(r'(?<=[.!?])\s+', probe):
            if len(part.split()) > 65:
                findings.append((where, kind, 'very long sentence '
                                 f'({len(part.split())} words)',
                                 part[:70] + '...'))

    print(f'checked {words:,} words, ~{sentences:,} sentences\n')
    if not findings:
        print('no typographic issues found')
        return 0
    seen = set()
    for where, kind, label, snippet in findings:
        key = (label, snippet)
        if key in seen:
            continue
        seen.add(key)
        print(f'[{where} / {kind}] {label}')
        print(f'    ...{snippet}...')
    print(f'\n{len(seen)} item(s) to review')
    return 0


MODULES = ['report_content', 'content_prahadhesvaryaa', 'content_senthamil',
           'content_haameed', 'content_ganesh', 'content_jayasubha']


if __name__ == '__main__':
    wanted = [a for a in sys.argv[1:] if not a.startswith('-')] or MODULES
    status = 0
    for name in wanted:
        rc = importlib.import_module(name)
        print(f'=== {name} ===')
        status |= main()
        print()
    sys.exit(status)
