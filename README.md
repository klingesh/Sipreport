# SIP Report

## Files

| File | What it is |
|---|---|
| `Lingesh K - SIP Report 2026.docx` | **The submission copy.** Open in Word and export to PDF. |
| `SIP-Report-2026.md` | Same text in Markdown, for reading/reviewing on GitHub. |
| `Internship Certificate.png` | Scan of the internship completion certificate, kept here for reference. It is **not** printed into the report. |
| `assets/issm-must-logo.jpg` | MUST + ISSM banner used on the title page. |
| `Aarti Chettiar-SIP Report .pdf`, `Final SIP KYR.pdf` | Seniors' reports, used only as references for structure and formatting. |
| `tools/report_content.py` | All report text lives here — edit this to change any wording. |
| `tools/build_report.py` | Renders the content into the `.docx` and `.md`. |
| `tools/docx_writer.py` | Minimal OOXML writer (no external packages needed). |
| `tools/verify_docx.py` | Structural check of the generated `.docx`. |
| `tools/lint_text.py` | Proof-reading pass over the report text. |

## Rebuilding after an edit

```sh
python3 tools/build_report.py
python3 tools/verify_docx.py "Lingesh K - SIP Report 2026.docx"
python3 tools/lint_text.py
```

## Notes on the document

- A4, Times New Roman 12 pt, 1.5 line spacing, justified; 1" margins with 1.25" on the
  binding edge.
- Layout follows the sample reports (`Final SIP KYR.pdf`, `Aarti Chettiar-SIP Report .pdf`):
  running header with `CHAPTER n` on the left and the chapter title on the right over a blue
  rule; running footer with `SUMMER INTERNSHIP PROJECT` on the left and the page number on
  the right under a blue rule. Front matter carries neither; page numbering restarts at 1
  from Chapter 1.
- The page numbers in the Table of Contents are Word `PAGEREF` fields, so they update
  themselves. If they show stale values, press `Ctrl+A` then `F9` in Word.
- The INTERNSHIP CERTIFICATE page carries the heading only, matching both sample reports —
  the certificate is attached as a separate sheet. To print the scan onto that page
  instead, set `EMBED_CERTIFICATE = True` in `tools/report_content.py` and rebuild.
