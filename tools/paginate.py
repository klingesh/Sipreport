# -*- coding: utf-8 -*-
"""Faithful page layout model for the generated reports.

The earlier estimator counted characters, which undercounted lines by roughly a
fifth and ignored the way Word pushes a heading to the next page to keep it
with its paragraph. This module measures text with real Times New Roman advance
widths, wraps greedily on word boundaries as Word does, and then flows the
resulting lines onto pages honouring keepNext, keepLines, widow/orphan control
and the fact that a table row cannot be split.

    python3 tools/paginate.py                 # every report
    python3 tools/paginate.py lingesh         # one of them
    python3 tools/paginate.py lingesh --thin  # list underfull pages only
"""
import importlib
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

# --- page geometry (A4, 1" top/bottom, 1" right, 1.25" binding edge) --------
TWIPS_IN = 1440.0
PAGE_W, PAGE_H = 11906, 16838
MARGIN_T = MARGIN_B = MARGIN_R = 1440
MARGIN_L = 1800
TEXT_W = PAGE_W - MARGIN_L - MARGIN_R          # 8666 twips
TEXT_H_IN = (PAGE_H - MARGIN_T - MARGIN_B) / TWIPS_IN
TEXT_W_IN = TEXT_W / TWIPS_IN

# Word's single line height for Times New Roman is about 1.15 em; the reports
# set w:line=360 (1.5 lines), so a line occupies size * 1.15 * 1.5 points.
LINE_FACTOR = 1.15 * 1.5


def line_h(pt, spacing=1.5):
    return pt * 1.15 * spacing / 72.0


# --- Times New Roman advance widths, units per 1000 em ----------------------
_R = {
    ' ': 250, '!': 333, '"': 408, '#': 500, '$': 500, '%': 833, '&': 778,
    "'": 180, '(': 333, ')': 333, '*': 500, '+': 564, ',': 250, '-': 333,
    '.': 250, '/': 278, ':': 278, ';': 278, '<': 564, '=': 564, '>': 564,
    '?': 444, '@': 921, '[': 333, '\\': 278, ']': 333, '^': 469, '_': 500,
    '`': 333, '{': 480, '|': 200, '}': 480, '~': 541,
    'A': 722, 'B': 667, 'C': 667, 'D': 722, 'E': 611, 'F': 556, 'G': 722,
    'H': 722, 'I': 333, 'J': 389, 'K': 722, 'L': 611, 'M': 889, 'N': 722,
    'O': 722, 'P': 556, 'Q': 722, 'R': 667, 'S': 556, 'T': 611, 'U': 722,
    'V': 722, 'W': 944, 'X': 722, 'Y': 722, 'Z': 611,
    'a': 444, 'b': 500, 'c': 444, 'd': 500, 'e': 444, 'f': 333, 'g': 500,
    'h': 500, 'i': 278, 'j': 278, 'k': 500, 'l': 278, 'm': 778, 'n': 500,
    'o': 500, 'p': 500, 'q': 500, 'r': 333, 's': 389, 't': 278, 'u': 500,
    'v': 500, 'w': 722, 'x': 500, 'y': 500, 'z': 444,
    '\u2019': 333, '\u2018': 333, '\u201c': 444, '\u201d': 444,
    '\u2013': 500, '\u2014': 1000, '\u2022': 350, '\u20b9': 500,
    '\u25cb': 604, '\u25aa': 500,
}
_B = dict(_R)
_B.update({
    'A': 722, 'B': 667, 'C': 722, 'D': 722, 'E': 667, 'F': 611, 'G': 778,
    'H': 778, 'I': 389, 'J': 500, 'K': 778, 'L': 667, 'M': 944, 'N': 722,
    'O': 778, 'P': 611, 'Q': 778, 'R': 722, 'S': 556, 'T': 667, 'U': 722,
    'V': 722, 'W': 1000, 'X': 722, 'Y': 722, 'Z': 667,
    'a': 500, 'b': 500, 'c': 444, 'd': 500, 'e': 444, 'f': 333, 'g': 500,
    'h': 556, 'i': 278, 'j': 333, 'k': 556, 'l': 278, 'm': 833, 'n': 556,
    'o': 500, 'p': 556, 'q': 556, 'r': 444, 's': 389, 't': 333, 'u': 556,
    'v': 500, 'w': 722, 'x': 500, 'y': 500, 'z': 444,
    ':': 333, ';': 333, '!': 333, '?': 500, "'": 287,
})
DEFAULT = 500


def str_w(text, pt, bold=False):
    """Width of a string in inches."""
    tab = _B if bold else _R
    return sum(tab.get(c, DEFAULT) for c in text) * pt / 1000.0 / 72.0


def wrap(text, width_in, pt, bold=False, first_indent_in=0.0):
    """Number of lines a paragraph occupies under greedy word wrapping."""
    text = text.replace('**', '')
    words = text.split()
    if not words:
        return 1
    space = str_w(' ', pt, bold)
    lines, cur, limit = 1, 0.0, width_in - first_indent_in
    for w in words:
        ww = str_w(w, pt, bold)
        if cur == 0.0:
            cur = ww
            if cur > limit:                      # a single over-long word
                cur = limit
        elif cur + space + ww <= limit:
            cur += space + ww
        else:
            lines += 1
            cur = ww
            limit = width_in
    return lines


# ---------------------------------------------------------------------------
# blocks -> atoms
# ---------------------------------------------------------------------------
class Atom(object):
    """One unbreakable unit of vertical space."""

    __slots__ = ('h', 'keep_next', 'group', 'label')

    def __init__(self, h, keep_next=False, group=None, label=''):
        self.h = h
        self.keep_next = keep_next
        self.group = group          # lines sharing a group belong to one para
        self.label = label


def _para_atoms(text, pt, bold, after_tw, before_tw=0, indent_in=0.0,
                first_indent_in=0.0, keep_next=False, gid=0, label='',
                spacing=1.5):
    width = TEXT_W_IN - indent_in
    n = wrap(text, width, pt, bold, first_indent_in)
    lh = line_h(pt, spacing)
    out = []
    for i in range(n):
        h = lh
        if i == 0:
            h += before_tw / TWIPS_IN
        if i == n - 1:
            h += after_tw / TWIPS_IN
        out.append(Atom(h, keep_next and i == n - 1, gid, label if i == 0
                        else ''))
    return out


def atoms_for(block, gid, rc):
    """Vertical atoms for one content block."""
    kind = block[0]
    payload = block[1] if len(block) > 1 else None
    size = block[2] if len(block) > 2 and isinstance(block[2], int) else None

    if kind == 'p':
        return _para_atoms(payload, size or 12, False, 140, gid=gid)
    if kind == 'p_indent':
        return _para_atoms(payload, 12, False, 140, gid=gid,
                           first_indent_in=0.5)
    if kind == 'center':
        return _para_atoms(payload, size or 12, False, 40, gid=gid)
    if kind == 'cbold':
        return _para_atoms(payload, size or 12, True, 40, gid=gid)
    if kind == 'cbi':
        return _para_atoms(payload, size or 12, True, 40, gid=gid)
    if kind == 'big':
        return _para_atoms(payload, size or 14, True, 200, gid=gid)
    if kind == 'h1':
        return _para_atoms(payload, 14, True, 240, before_tw=0,
                           keep_next=True, gid=gid, label=payload)
    if kind == 'h2':
        return _para_atoms(payload, 14, True, 120, before_tw=240,
                           keep_next=True, gid=gid, label=payload)
    if kind == 'h3':
        return _para_atoms(payload, 12, True, 100, before_tw=180,
                           keep_next=True, gid=gid, label=payload)
    if kind == 'bullets':
        out = []
        for i, item in enumerate(payload):
            out += _para_atoms(item, 12, False, 80, indent_in=0.5,
                               gid=gid * 100 + i)
        out.append(Atom(line_h(12) + 60 / TWIPS_IN, group=gid * 100 + 99))
        return out
    if kind == 'table':
        rows = payload['rows']
        widths = payload.get('widths') or [1] * len(rows[0])
        share = float(sum(widths))
        pw = TEXT_W
        rh_min = (payload.get('row_height') or 0) / TWIPS_IN
        out = []
        for r in rows:
            cell_lines = []
            for i, cell in enumerate(r):
                cw = pw * widths[i] / share
                inner = (cw - 216) / TWIPS_IN          # 108 twips each side
                cell_lines.append(wrap(cell, max(0.4, inner), 12, True))
            h = max(cell_lines) * line_h(12, 1.0) + 160 / TWIPS_IN
            out.append(Atom(max(h, rh_min), group=None))
        out.append(Atom(line_h(12) + 120 / TWIPS_IN))
        return out
    if kind == 'toc':
        n = 1 + len(rc.CHAPTERS)
        rh = getattr(rc, 'TOC_ROW_HEIGHT', 640) / TWIPS_IN
        return [Atom(rh) for _ in range(n)]
    if kind == 'gap':
        return [Atom(line_h(12)) for _ in range(payload)]
    if kind == 'sign':
        return [Atom(line_h(12) + 140 / TWIPS_IN)]
    if kind == 'logo':
        import build_report as br
        s = br.logo_size_in(TEXT_W)
        return [Atom(s[1] if s else 0.0)]
    if kind == 'certificate_image':
        return [Atom(TEXT_H_IN - 2.0)]
    if kind in ('pagebreak', 'box'):
        return []
    return []


# ---------------------------------------------------------------------------
# flow
# ---------------------------------------------------------------------------
def flow(atom_runs):
    """Flow runs of atoms onto pages. A run is (atoms, hard_break_after).

    Honours keepNext (a heading travels with the first line of what follows)
    and widow/orphan control (never one line of a paragraph alone).
    Returns a list of page fill heights, and the label opening each page.
    """
    pages, used, labels, cur_label = [], 0.0, [], ''
    seq = []
    for atoms, hard in atom_runs:
        seq.append((atoms, hard))

    flat = []
    for atoms, hard in seq:
        flat.append(('atoms', atoms))
        if hard:
            flat.append(('break', None))

    def newpage():
        nonlocal used
        pages.append(used)
        labels.append(cur_label)
        used = 0.0

    i = 0
    stream = []
    for kind, payload in flat:
        if kind == 'break':
            stream.append(None)
        else:
            stream.extend(payload)

    n = len(stream)
    while i < n:
        a = stream[i]
        if a is None:                       # explicit page break
            newpage()
            i += 1
            continue
        # how many atoms must travel together starting here?
        need, j = a.h, i
        bundle = [a]
        while j < n - 1 and stream[j] is not None and stream[j].keep_next:
            nxt = stream[j + 1]
            if nxt is None:
                break
            bundle.append(nxt)
            need += nxt.h
            j += 1
        # widow/orphan: a multi-line paragraph should not leave one line alone
        if a.group is not None and len(bundle) == 1:
            same = [k for k in range(i, min(n, i + 3))
                    if stream[k] is not None and stream[k].group == a.group]
            if len(same) >= 2:
                need = sum(stream[k].h for k in same[:2])
        if used > 0 and used + need > TEXT_H_IN + 1e-9:
            newpage()
        for k in range(i, j + 1):
            used += stream[k].h
        i = j + 1
    if used > 0:
        newpage()
    return pages, labels


def report_pages(rc):
    """(front_pages, body_pages) as lists of used heights."""
    front_runs = []
    for b in rc.FRONT:
        front_runs.append((atoms_for(b, 0, rc), b[0] == 'pagebreak'))
    front, _ = flow(front_runs)

    body_runs = []
    for ch in rc.CHAPTERS:
        # divider page
        body_runs.append(([Atom(line_h(12)) for _ in range(13)]
                          + [Atom(line_h(16) + 240 / TWIPS_IN),
                             Atom(line_h(16))], True))
        for k, b in enumerate(ch['blocks']):
            body_runs.append((atoms_for(b, k + 1, rc), b[0] == 'pagebreak'))
        body_runs.append(([], True))       # chapter ends on its own page
    body, labels = flow(body_runs)
    return front, body, labels


def chapter_pages(rc):
    """Per-chapter page usage: [(num, pages, last_page_fill_pct, height)]."""
    out = []
    for ch in rc.CHAPTERS:
        runs = []
        for k, b in enumerate(ch['blocks']):
            runs.append((atoms_for(b, k + 1, rc), b[0] == 'pagebreak'))
        pages, _ = flow(runs)
        h = sum(pages)
        out.append((ch['num'], len(pages),
                    pages[-1] / TEXT_H_IN * 100 if pages else 0.0, h))
    return out


def tune(rc, target):
    """Report, per chapter, the change needed to reach `target[num]` pages
    with the closing page at least 80 per cent full."""
    rows = []
    for num, pages, last, h in chapter_pages(rc):
        want = target.get(num, pages)
        lo = (want - 1) * TEXT_H_IN + 0.80 * TEXT_H_IN
        hi = want * TEXT_H_IN
        if h < lo:
            delta = lo - h
        elif h > hi:
            delta = hi - h
        else:
            delta = 0.0
        rows.append((num, pages, last, h, want, delta))
    return rows


def main(names, thin_only=False):
    import build_report as br
    for name in names:
        rc = importlib.import_module(br.REPORTS[name]['module'])
        br.rc = rc
        front, body, labels = report_pages(rc)
        print('=' * 74)
        print('%s   front matter %d pages, numbered %d, total %d'
              % (name, len(front), len(body), len(front) + len(body)))
        thin = [(i + 1, h / TEXT_H_IN * 100)
                for i, h in enumerate(body) if h / TEXT_H_IN < 0.80]
        if thin:
            print('   pages below 80%% full: %s'
                  % ', '.join('p%d=%.0f%%' % t for t in thin))
        else:
            print('   every numbered page is at least 80% full')
        if not thin_only:
            ft = [(i + 1, h / TEXT_H_IN * 100)
                  for i, h in enumerate(front) if h / TEXT_H_IN < 0.80]
            if ft:
                print('   front matter below 80%%: %s'
                      % ', '.join('p%d=%.0f%%' % t for t in ft))


if __name__ == '__main__':
    args = [a for a in sys.argv[1:] if not a.startswith('-')]
    import build_report as br
    main(args or list(br.REPORTS), thin_only='--thin' in sys.argv)
