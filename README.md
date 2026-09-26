# SIP Reports

Seven Summer Internship Project reports, all built to the format of the sample reports in
this repository.

| Report | Submission copy | Text for review |
|---|---|---|
| Lingesh K (OSI2509030) — S. Ravi & Associates, Chartered Accountants | `Lingesh K - SIP Report 2026.docx` | `SIP-Report-2026.md` |
| Prahadhesvaryaa K. S. (OSI2509093) — Neuberg Diagnostics Private Limited, Internal Audit | `Prahadhesvaryaa K S - SIP Report 2026.docx` | `SIP-Report-2026-Prahadhesvaryaa.md` |
| Senthamil Selvan V (OSI2509099) — ACTC Studio Pvt. Ltd., Business Development & Events | `Senthamil Selvan V - SIP Report 2026.docx` | `SIP-Report-2026-Senthamil.md` |
| Haameed Abdur Rahman SK (OSI2509017) — Q-Up Private Limited, Business Development & Operations | `Haameed Abdur Rahman SK - SIP Report 2026.docx` | `SIP-Report-2026-Haameed.md` |
| Ganeshkumar S — Doodleblue Innovations Private Limited, Digital Marketing | `Ganeshkumar S - SIP Report 2026.docx` | `SIP-Report-2026-Ganesh.md` |
| Jayasubha S (OSI2511007) — Ashok Leyland Limited, Human Resources & Industrial Relations | `Jayasubha S - SIP Report 2026.docx` | `SIP-Report-2026-Jayasubha.md` |
| Aarnav Rupesh. K (ISSMCHNM250112) — Ecosoft Zolutions Pvt Ltd, Sales / Business Development | `Aarnav Rupesh K - SIP Report 2026.docx` | `SIP-Report-2026-Aarnav.md` |

> **Aarnav's report has placeholders to fill in.** The ISSM office bearers were not
> supplied and were deliberately not copied from another student's report, so the
> Chairman, Founder and Academic Head appear as `[NAME OF CHAIRMAN]`,
> `[NAME OF FOUNDER AND MANAGING DIRECTOR]` and `[NAME OF ACADEMIC HEAD]`. Three
> `[TO BE PROVIDED]` markers cover the company history, an industry guide's name and
> the official subject titles. **His register number also needs settling:** the
> internship certificate reads `ISSMCHNM250112` and is used here, but his written
> brief gave `OSI2511003`.

> **Lingesh, Prahadhesvaryaa and Haameed's reports were revised**: every
> person's name in bold, "Ms." rather than "Mrs." for the Academic Head, a single
> Times New Roman face throughout, a one-page executive summary, a contents table
> that fills its page, no shading in any table, fewer bullet lists in favour of
> prose, 52 numbered pages, and every page at least 80% full apart from the six
> chapter divider pages and the internship certificate sheet, which carry a
> heading only by design. The other three reports are unchanged; rebuilding them
> would pick up the shared writer changes (no table shading, Times New Roman
> bullet glyphs).

`tools/paginate.py` is the layout model to trust. It measures text with real
Times New Roman advance widths, wraps on word boundaries as Word does, and
models `keepNext` and widow/orphan control, so it reports page counts and
per-page fill that match Word closely. The older `estimate_pages` in
`build_report.py` counts characters and runs several pages short.

> **Ganeshkumar's report still has four blanks to fill in** — register number, the two
> internship certificate dates and the industry mentor's name. They appear as
> `[REGISTER NUMBER]`, `[START DATE]`, `[END DATE]` and `[NAME OF INDUSTRY MENTOR]` in
> `tools/content_ganesh.py`; replace them there and rebuild.

## Other files

| File | What it is |
|---|---|
| `Internship Certificate.png` | Lingesh's internship certificate scan, kept for reference. It is **not** printed into the report. |
| `assets/issm-must-logo.jpg` | MUST + ISSM banner used on the title pages. |
| `Aarti Chettiar-SIP Report .pdf`, `Final SIP KYR.pdf` | Seniors' reports, used only as references for structure and formatting. |
| `tools/report_content.py` | All of Lingesh's report text — edit this to change any wording. |
| `tools/content_prahadhesvaryaa.py` | All of Prahadhesvaryaa's report text. |
| `tools/content_senthamil.py` | All of Senthamil's report text. |
| `tools/content_haameed.py` | All of Haameed's report text. |
| `tools/content_ganesh.py` | All of Ganeshkumar's report text. |
| `tools/content_jayasubha.py` | All of Jayasubha's report text. |
| `tools/content_aarnav.py` | All of Aarnav's report text. |
| `tools/paginate.py` | Faithful page layout model — the page counts to trust. |
| `Ganesh chapther 1.docx` | Ganeshkumar's original five-chapter draft, kept as the source for his report. |
| `Jayasubha_S_SIP_Report.pdf` | Jayasubha's original draft, kept as the source for her report. |
| `tools/build_report.py` | Renders a content module into a `.docx` and a `.md`. |
| `tools/docx_writer.py` | Minimal OOXML writer (no external packages needed). |
| `tools/verify_docx.py` | Structural check of a generated `.docx`. |
| `tools/lint_text.py` | Proof-reading pass over the report text. |
| `tools/compare_docx.py` | Checks that two generated reports share the same formatting and structure. |
| `tools/audit_fonts.py` | Checks every font size and weight against the sample report's measured specification. |

## Rebuilding after an edit

```sh
python3 tools/build_report.py                   # all six reports
python3 tools/build_report.py prahadhesvaryaa   # just one
python3 tools/verify_docx.py "Prahadhesvaryaa K S - SIP Report 2026.docx"
python3 tools/lint_text.py
python3 tools/compare_docx.py "Lingesh K - SIP Report 2026.docx" "Prahadhesvaryaa K S - SIP Report 2026.docx"
```

## Notes on the documents

- A4, Times New Roman 12 pt, 1.5 line spacing, justified; 1" margins with 1.25" on the
  binding edge.
- Running header with `CHAPTER n` on the left and the chapter title on the right over a blue
  rule; running footer with `SUMMER INTERNSHIP PROJECT` on the left and the page number on
  the right under a blue rule. Front matter carries neither; page numbering restarts at 1
  from Chapter 1.
- The page numbers in each Table of Contents are Word `PAGEREF` fields, so they update
  themselves. If they show stale values, press `Ctrl+A` then `F9` in Word.
- The INTERNSHIP CERTIFICATE page carries the heading only, as in both sample reports — the
  certificate is attached as a separate sheet. To print a scan onto that page instead, set
  `EMBED_CERTIFICATE = True` in the relevant content module and rebuild.
