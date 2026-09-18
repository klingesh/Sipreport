"""
Minimal, dependency-free .docx (OOXML) writer.

Built by hand with zipfile because the sandbox has no network access and
therefore no python-docx. Supports everything this report needs:
  * Times New Roman body text, justified, 1.5 line spacing
  * multiple sections, each with its own running header + page numbers
  * headings, centred text, bullet lists, bordered tables, page breaks
  * optional JPEG/PNG image embedding (dimensions parsed manually)
"""
import os
import re
import struct
import zipfile

EMU_PER_INCH = 914400
TWIPS_PER_INCH = 1440

W = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'


def esc(text):
    return (str(text).replace('&', '&amp;').replace('<', '&lt;')
            .replace('>', '&gt;').replace('"', '&quot;'))


# --------------------------------------------------------------------------
# runs and paragraphs
# --------------------------------------------------------------------------
def run(text, bold=False, italic=False, underline=False, size=None,
        caps=False, color=None, font=None):
    """size is in points."""
    props = []
    if font:
        props.append(f'<w:rFonts w:ascii="{font}" w:hAnsi="{font}" w:cs="{font}"/>')
    if bold:
        props.append('<w:b/>')
    if italic:
        props.append('<w:i/>')
    if underline:
        props.append('<w:u w:val="single"/>')
    if caps:
        props.append('<w:caps/>')
    if color:
        props.append(f'<w:color w:val="{color}"/>')
    if size:
        half = int(round(size * 2))
        props.append(f'<w:sz w:val="{half}"/><w:szCs w:val="{half}"/>')
    rpr = f'<w:rPr>{"".join(props)}</w:rPr>' if props else ''
    out = []
    # keep tabs and manual line breaks meaningful
    parts = str(text).split('\n')
    for i, part in enumerate(parts):
        if i:
            out.append('<w:br/>')
        for j, chunk in enumerate(part.split('\t')):
            if j:
                out.append('<w:tab/>')
            if chunk:
                out.append(f'<w:t xml:space="preserve">{esc(chunk)}</w:t>')
    return f'<w:r>{rpr}{"".join(out)}</w:r>'


FIELD_RE = re.compile(r'\{\{PAGEREF ([A-Za-z0-9_]+)\|([^}]*)\}\}')


def bookmark(name, bid):
    """A zero-length bookmark, to be placed inside a paragraph."""
    return (f'<w:bookmarkStart w:id="{bid}" w:name="{name}"/>'
            f'<w:bookmarkEnd w:id="{bid}"/>')


def pageref_field(name, fallback=''):
    """Cross-reference to the page a bookmark sits on; Word recalculates it."""
    return (f'<w:fldSimple w:instr=" PAGEREF {name} \\h ">'
            f'<w:r><w:rPr><w:noProof/></w:rPr>'
            f'<w:t>{esc(fallback)}</w:t></w:r></w:fldSimple>')


def rich(text, **kwargs):
    """Turn a string into runs, honouring **bold** and {{PAGEREF x|n}} tokens."""
    out = []
    pos = 0
    text = str(text)
    for m in FIELD_RE.finditer(text):
        out.append(_bold_runs(text[pos:m.start()], kwargs))
        out.append(pageref_field(m.group(1), m.group(2)))
        pos = m.end()
    out.append(_bold_runs(text[pos:], kwargs))
    return ''.join(out)


def _bold_runs(text, kwargs):
    out = []
    for i, chunk in enumerate(text.split('**')):
        if not chunk:
            continue
        opts = dict(kwargs)
        if i % 2:
            opts['bold'] = True
        out.append(run(chunk, **opts))
    return ''.join(out)


def para(content='', jc=None, before=0, after=0, line=360, ind_left=None,
         ind_hanging=None, keep_next=False, border_bottom=False, tabs=None,
         page_break_before=False, style=None, num_id=None, num_level=0,
         contextual=False):
    """Assemble a <w:p>. Child order inside w:pPr must follow the schema."""
    # NB: children of w:pPr must appear in the order defined by CT_PPr:
    # pStyle, keepNext, keepLines, pageBreakBefore, numPr, pBdr, tabs,
    # spacing, ind, contextualSpacing, jc
    p = []
    if style:
        p.append(f'<w:pStyle w:val="{style}"/>')
    if keep_next:
        p.append('<w:keepNext/><w:keepLines/>')
    if page_break_before:
        p.append('<w:pageBreakBefore/>')
    if num_id is not None:
        p.append(f'<w:numPr><w:ilvl w:val="{num_level}"/>'
                 f'<w:numId w:val="{num_id}"/></w:numPr>')
    if border_bottom:
        p.append('<w:pBdr><w:bottom w:val="single" w:sz="6" w:space="1" '
                 'w:color="000000"/></w:pBdr>')
    if tabs:
        stops = ''.join(
            f'<w:tab w:val="{val}" w:pos="{pos}"/>' for val, pos in tabs)
        p.append(f'<w:tabs>{stops}</w:tabs>')
    p.append(f'<w:spacing w:before="{before}" w:after="{after}" '
             f'w:line="{line}" w:lineRule="auto"/>')
    if ind_left is not None or ind_hanging is not None:
        bits = []
        if ind_left is not None:
            bits.append(f'w:left="{ind_left}"')
        if ind_hanging is not None:
            bits.append(f'w:hanging="{ind_hanging}"')
        p.append(f'<w:ind {" ".join(bits)}/>')
    if contextual:
        p.append('<w:contextualSpacing/>')
    if jc:
        p.append(f'<w:jc w:val="{jc}"/>')
    ppr = f'<w:pPr>{"".join(p)}</w:pPr>'
    return f'<w:p>{ppr}{content}</w:p>'


def page_break():
    return ('<w:p><w:pPr><w:spacing w:before="0" w:after="0" w:line="240" '
            'w:lineRule="auto"/></w:pPr><w:r><w:br w:type="page"/></w:r></w:p>')


def page_field():
    return ('<w:fldSimple w:instr=" PAGE   \\* MERGEFORMAT ">'
            '<w:r><w:rPr><w:noProof/></w:rPr><w:t>1</w:t></w:r></w:fldSimple>')


# --------------------------------------------------------------------------
# tables
# --------------------------------------------------------------------------
def table(rows, widths=None, header=True, font_size=11, align='left',
          shade='D9D9D9', page_width=9360):
    """rows: list of list of cell strings. widths: list of relative ints."""
    ncols = max(len(r) for r in rows)
    if not widths:
        widths = [1] * ncols
    total = sum(widths)
    abs_w = [int(page_width * w / total) for w in widths]

    grid = ''.join(f'<w:gridCol w:w="{w}"/>' for w in abs_w)
    borders = ('<w:tblBorders>'
               + ''.join(f'<w:{side} w:val="single" w:sz="6" w:space="0" '
                         f'w:color="000000"/>'
                         for side in ('top', 'left', 'bottom', 'right',
                                      'insideH', 'insideV'))
               + '</w:tblBorders>')
    tbl = [f'<w:tblPr><w:tblStyle w:val="TableGrid"/>'
           f'<w:tblW w:w="{page_width}" w:type="dxa"/>'
           f'<w:jc w:val="{align}"/>{borders}'
           f'<w:tblLayout w:type="fixed"/>'
           f'<w:tblCellMar>'
           f'<w:top w:w="60" w:type="dxa"/><w:left w:w="108" w:type="dxa"/>'
           f'<w:bottom w:w="60" w:type="dxa"/><w:right w:w="108" w:type="dxa"/>'
           f'</w:tblCellMar></w:tblPr><w:tblGrid>{grid}</w:tblGrid>']

    for r_i, row in enumerate(rows):
        is_head = header and r_i == 0
        cells = []
        for c_i in range(ncols):
            text = row[c_i] if c_i < len(row) else ''
            shading = (f'<w:shd w:val="clear" w:color="auto" w:fill="{shade}"/>'
                       if is_head else '')
            body = para(rich(text, bold=is_head, size=font_size),
                        jc='center' if is_head else 'left',
                        before=20, after=20, line=240)
            cells.append(
                f'<w:tc><w:tcPr><w:tcW w:w="{abs_w[c_i]}" w:type="dxa"/>'
                f'{shading}<w:vAlign w:val="center"/></w:tcPr>{body}</w:tc>')
        # CT_TrPr order: cantSplit before tblHeader
        trpr = ('<w:trPr><w:cantSplit/><w:tblHeader/></w:trPr>' if is_head
                else '<w:trPr><w:cantSplit/></w:trPr>')
        tbl.append(f'<w:tr>{trpr}{"".join(cells)}</w:tr>')
    return f'<w:tbl>{"".join(tbl)}</w:tbl>'


# --------------------------------------------------------------------------
# images
# --------------------------------------------------------------------------
def image_size(path):
    """Return (width, height) in pixels for JPEG/PNG without external libs."""
    with open(path, 'rb') as fh:
        data = fh.read()
    if data[:8] == b'\x89PNG\r\n\x1a\n':
        w, h = struct.unpack('>II', data[16:24])
        return w, h
    if data[:2] == b'\xff\xd8':
        i = 2
        while i < len(data) - 9:
            if data[i] != 0xFF:
                i += 1
                continue
            marker = data[i + 1]
            if marker in (0xD8, 0x01) or 0xD0 <= marker <= 0xD7:
                i += 2
                continue
            seg_len = struct.unpack('>H', data[i + 2:i + 4])[0]
            if 0xC0 <= marker <= 0xCF and marker not in (0xC4, 0xC8, 0xCC):
                h, w = struct.unpack('>HH', data[i + 5:i + 9])
                return w, h
            i += 2 + seg_len
    raise ValueError(f'unsupported image: {path}')


def drawing(rel_id, cx, cy, name='Picture'):
    return f'''<w:r><w:drawing><wp:inline distT="0" distB="0" distL="0" distR="0">
<wp:extent cx="{cx}" cy="{cy}"/><wp:effectExtent l="0" t="0" r="0" b="0"/>
<wp:docPr id="{abs(hash(rel_id)) % 100000 + 1}" name="{esc(name)}"/>
<wp:cNvGraphicFramePr><a:graphicFrameLocks xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" noChangeAspect="1"/></wp:cNvGraphicFramePr>
<a:graphic xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"><a:graphicData uri="http://schemas.openxmlformats.org/drawingml/2006/picture">
<pic:pic xmlns:pic="http://schemas.openxmlformats.org/drawingml/2006/picture">
<pic:nvPicPr><pic:cNvPr id="0" name="{esc(name)}"/><pic:cNvPicPr/></pic:nvPicPr>
<pic:blipFill><a:blip r:embed="{rel_id}"/><a:stretch><a:fillRect/></a:stretch></pic:blipFill>
<pic:spPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="{cx}" cy="{cy}"/></a:xfrm>
<a:prstGeom prst="rect"><a:avLst/></a:prstGeom></pic:spPr></pic:pic>
</a:graphicData></a:graphic></wp:inline></w:drawing></w:r>'''


# --------------------------------------------------------------------------
# document assembly
# --------------------------------------------------------------------------
class Section:
    def __init__(self, header_left=None, header_right=None, page_numbers=False,
                 restart_at=None):
        self.header_left = header_left
        self.header_right = header_right
        self.page_numbers = page_numbers
        self.restart_at = restart_at
        self.body = []

    def add(self, xml):
        self.body.append(xml)


class Document:
    PAGE_W = 12240          # 8.5" letter -> A4 is 11906 x 16838
    PAGE_H = 15840

    def __init__(self, a4=True, margins=(1440, 1440, 1440, 1440), title=''):
        if a4:
            self.PAGE_W, self.PAGE_H = 11906, 16838
        self.margins = margins        # top, right, bottom, left
        self.sections = []
        self.images = []              # (rel_id, filename, bytes)
        self.title = title

    @property
    def content_width(self):
        return self.PAGE_W - self.margins[1] - self.margins[3]

    def section(self, **kwargs):
        s = Section(**kwargs)
        self.sections.append(s)
        return s

    def add_image(self, path):
        idx = len(self.images) + 1
        ext = os.path.splitext(path)[1].lower().lstrip('.')
        ext = 'jpeg' if ext in ('jpg', 'jpeg') else ext
        name = f'image{idx}.{ext}'
        with open(path, 'rb') as fh:
            self.images.append((f'rIdImg{idx}', name, fh.read()))
        return f'rIdImg{idx}'

    # ---------------- parts ----------------
    def _sect_pr(self, sec, header_rel):
        bits = []
        if header_rel:
            bits.append(f'<w:headerReference w:type="default" r:id="{header_rel}"/>')
        bits.append(f'<w:pgSz w:w="{self.PAGE_W}" w:h="{self.PAGE_H}"/>')
        t, r, b, l = self.margins
        bits.append(f'<w:pgMar w:top="{t}" w:right="{r}" w:bottom="{b}" '
                    f'w:left="{l}" w:header="720" w:footer="720" w:gutter="0"/>')
        if sec.restart_at is not None:
            bits.append(f'<w:pgNumType w:start="{sec.restart_at}"/>')
        bits.append('<w:cols w:space="720"/><w:docGrid w:linePitch="360"/>')
        return f'<w:sectPr>{"".join(bits)}</w:sectPr>'

    def _header_xml(self, sec):
        width = self.content_width
        line1 = para(
            run(sec.header_left or '', bold=True, size=10)
            + ('<w:r><w:tab/></w:r>' if sec.header_right else '')
            + (run(sec.header_right, bold=True, size=10) if sec.header_right else ''),
            jc='left', line=240, after=0,
            tabs=[('right', width)])
        line2 = para(page_field() if sec.page_numbers else '',
                     jc='right', line=240, after=0, border_bottom=True)
        return ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
                f'<w:hdr xmlns:w="{W}" xmlns:r="http://schemas.openxmlformats.org'
                '/officeDocument/2006/relationships">'
                f'{line1}{line2}</w:hdr>')

    def _document_xml(self):
        body = []
        for i, sec in enumerate(self.sections):
            header_rel = f'rIdHdr{i + 1}' if (sec.header_left or sec.page_numbers) else None
            sect_pr = self._sect_pr(sec, header_rel)
            body.extend(sec.body)
            if i < len(self.sections) - 1:
                # section break carried on an empty paragraph
                body.append(f'<w:p><w:pPr>{sect_pr}</w:pPr></w:p>')
            else:
                body.append(sect_pr)
        return ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
                '<w:document '
                f'xmlns:w="{W}" '
                'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" '
                'xmlns:wp="http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing" '
                'xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" '
                'xmlns:pic="http://schemas.openxmlformats.org/drawingml/2006/picture">'
                f'<w:body>{"".join(body)}</w:body></w:document>')

    def _styles_xml(self):
        return f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:styles xmlns:w="{W}">
<w:docDefaults><w:rPrDefault><w:rPr>
<w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:eastAsia="Times New Roman" w:cs="Times New Roman"/>
<w:sz w:val="24"/><w:szCs w:val="24"/><w:lang w:val="en-IN"/>
</w:rPr></w:rPrDefault><w:pPrDefault><w:pPr>
<w:spacing w:after="120" w:line="360" w:lineRule="auto"/><w:jc w:val="both"/>
</w:pPr></w:pPrDefault></w:docDefaults>
<w:style w:type="paragraph" w:default="1" w:styleId="Normal">
<w:name w:val="Normal"/><w:qFormat/></w:style>
<w:style w:type="paragraph" w:styleId="ListParagraph">
<w:name w:val="List Paragraph"/><w:basedOn w:val="Normal"/><w:qFormat/>
<w:pPr><w:ind w:left="720"/><w:contextualSpacing/></w:pPr></w:style>
<w:style w:type="table" w:styleId="TableGrid"><w:name w:val="Table Grid"/>
<w:tblPr><w:tblBorders>
<w:top w:val="single" w:sz="6" w:space="0" w:color="000000"/>
<w:left w:val="single" w:sz="6" w:space="0" w:color="000000"/>
<w:bottom w:val="single" w:sz="6" w:space="0" w:color="000000"/>
<w:right w:val="single" w:sz="6" w:space="0" w:color="000000"/>
<w:insideH w:val="single" w:sz="6" w:space="0" w:color="000000"/>
<w:insideV w:val="single" w:sz="6" w:space="0" w:color="000000"/>
</w:tblBorders></w:tblPr></w:style>
<w:style w:type="character" w:styleId="Hyperlink"><w:name w:val="Hyperlink"/>
<w:rPr><w:color w:val="0563C1"/><w:u w:val="single"/></w:rPr></w:style>
</w:styles>'''

    def _numbering_xml(self):
        levels = []
        for lvl in range(3):
            # level 0 and 2 use Symbol bullets, level 1 uses a hollow bullet
            text = {0: '\uf0b7', 1: 'o', 2: '\uf0a7'}[lvl]
            font = 'Symbol' if lvl == 0 else ('Courier New' if lvl == 1
                                             else 'Wingdings')
            levels.append(f'''<w:lvl w:ilvl="{lvl}"><w:start w:val="1"/>
<w:numFmt w:val="bullet"/><w:lvlText w:val="{text}"/><w:lvlJc w:val="left"/>
<w:pPr><w:ind w:left="{720 + lvl * 360}" w:hanging="360"/></w:pPr>
<w:rPr><w:rFonts w:ascii="{font}" w:hAnsi="{font}" w:hint="default"/></w:rPr></w:lvl>''')
        return f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:numbering xmlns:w="{W}">
<w:abstractNum w:abstractNumId="0"><w:multiLevelType w:val="hybridMultilevel"/>
{''.join(levels)}</w:abstractNum>
<w:num w:numId="1"><w:abstractNumId w:val="0"/></w:num>
</w:numbering>'''

    def _settings_xml(self):
        return f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:settings xmlns:w="{W}">
<w:zoom w:percent="100"/><w:defaultTabStop w:val="720"/>
<w:characterSpacingControl w:val="doNotCompress"/>
<w:updateFields w:val="true"/>
<w:compat><w:compatSetting w:name="compatibilityMode" w:val="15"
w:uri="http://schemas.microsoft.com/office/word" /></w:compat>
</w:settings>'''

    def save(self, path):
        n_sections = len(self.sections)
        headers = {}
        for i, sec in enumerate(self.sections):
            if sec.header_left or sec.page_numbers:
                headers[f'rIdHdr{i + 1}'] = (f'header{i + 1}.xml',
                                             self._header_xml(sec))

        ct = ['<?xml version="1.0" encoding="UTF-8" standalone="yes"?>',
              '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">',
              '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>',
              '<Default Extension="xml" ContentType="application/xml"/>',
              '<Default Extension="jpeg" ContentType="image/jpeg"/>',
              '<Default Extension="png" ContentType="image/png"/>',
              '<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>',
              '<Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>',
              '<Override PartName="/word/settings.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.settings+xml"/>',
              '<Override PartName="/word/numbering.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.numbering+xml"/>',
              '<Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>',
              '<Override PartName="/docProps/app.xml" ContentType="application/vnd.openxmlformats-officedocument.extended-properties+xml"/>']
        for rel, (fname, _) in headers.items():
            ct.append(f'<Override PartName="/word/{fname}" ContentType='
                      '"application/vnd.openxmlformats-officedocument.wordprocessingml.header+xml"/>')
        ct.append('</Types>')

        rels = f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/>
<Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties" Target="docProps/app.xml"/>
</Relationships>'''

        doc_rels = ['<?xml version="1.0" encoding="UTF-8" standalone="yes"?>',
                    '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">',
                    '<Relationship Id="rIdStyles" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>',
                    '<Relationship Id="rIdSettings" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/settings" Target="settings.xml"/>',
                    '<Relationship Id="rIdNum" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/numbering" Target="numbering.xml"/>']
        for rel, (fname, _) in headers.items():
            doc_rels.append(f'<Relationship Id="{rel}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/header" Target="{fname}"/>')
        for rel, fname, _ in self.images:
            doc_rels.append(f'<Relationship Id="{rel}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image" Target="media/{fname}"/>')
        doc_rels.append('</Relationships>')

        core = f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties"
xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
<dc:title>{esc(self.title)}</dc:title><dc:creator>Lingesh K</dc:creator>
<cp:lastModifiedBy>Lingesh K</cp:lastModifiedBy></cp:coreProperties>'''

        app = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties"
xmlns:vt="http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes">
<Application>Microsoft Office Word</Application></Properties>'''

        os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
        with zipfile.ZipFile(path, 'w', zipfile.ZIP_DEFLATED) as z:
            z.writestr('[Content_Types].xml', '\n'.join(ct))
            z.writestr('_rels/.rels', rels)
            z.writestr('word/document.xml', self._document_xml())
            z.writestr('word/styles.xml', self._styles_xml())
            z.writestr('word/settings.xml', self._settings_xml())
            z.writestr('word/numbering.xml', self._numbering_xml())
            z.writestr('word/_rels/document.xml.rels', '\n'.join(doc_rels))
            for rel, (fname, xml) in headers.items():
                z.writestr(f'word/{fname}', xml)
            for rel, fname, blob in self.images:
                z.writestr(f'word/media/{fname}', blob)
            z.writestr('docProps/core.xml', core)
            z.writestr('docProps/app.xml', app)
        return path
