# SIP Reports

Two Summer Internship Project reports, both built to the format of the sample reports in
this repository.

| Report | Submission copy | Text for review |
|---|---|---|
| Lingesh K (OSI2509030) — S. Ravi & Associates, Chartered Accountants | `Lingesh K - SIP Report 2026.docx` | `SIP-Report-2026.md` |
| Prahadhesvaryaa K. S. (OSI2509093) — Neuberg Diagnostics Private Limited, Internal Audit | `Prahadhesvaryaa K S - SIP Report 2026.docx` | `SIP-Report-2026-Prahadhesvaryaa.md` |

## Other files

| File | What it is |
|---|---|
| `Internship Certificate.png` | Lingesh's internship certificate scan, kept for reference. It is **not** printed into the report. |
| `assets/issm-must-logo.jpg` | MUST + ISSM banner used on the title pages. |
| `Aarti Chettiar-SIP Report .pdf`, `Final SIP KYR.pdf` | Seniors' reports, used only as references for structure and formatting. |
| `tools/report_content.py` | All of Lingesh's report text — edit this to change any wording. |
| `tools/content_prahadhesvaryaa.py` | All of Prahadhesvaryaa's report text. |
| `tools/build_report.py` | Renders a content module into a `.docx` and a `.md`. |
| `tools/docx_writer.py` | Minimal OOXML writer (no external packages needed). |
| `tools/verify_docx.py` | Structural check of a generated `.docx`. |
| `tools/lint_text.py` | Proof-reading pass over the report text. |

## Rebuilding after an edit

```sh
python3 tools/build_report.py                   # both reports
python3 tools/build_report.py prahadhesvaryaa   # just one
python3 tools/verify_docx.py "Prahadhesvaryaa K S - SIP Report 2026.docx"
python3 tools/lint_text.py
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
