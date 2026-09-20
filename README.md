# SIP Report

## Files

| File | What it is |
|---|---|
| `Lingesh K - SIP Report 2026.docx` | **The submission copy.** Open in Word and export to PDF. |
| `SIP-Report-2026.md` | Same text in Markdown, for reading/reviewing on GitHub. |
| `Internship Certificate.png` | Scan of the internship completion certificate, embedded in the report. |
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
- Front matter is unnumbered; page numbering restarts at 1 from Chapter 1, shown in the
  running header along with the chapter name.
- The page numbers in the Table of Contents are Word `PAGEREF` fields, so they update
  themselves. If they show stale values, press `Ctrl+A` then `F9` in Word.
- The certificate scan is embedded automatically. To swap in a different scan, overwrite
  `Internship Certificate.png` or add `assets/internship-certificate.png`, then rebuild.
