# SIP Report — Lingesh K (OSI2509030)

Summer Internship Project report, MBA (Finance), ISSM Business School / Indian School of
Science and Management, Chennai.

Internship: **M/s S. Ravi & Associates, Chartered Accountants**, Mylapore, Chennai
Domain: Accounting and Finance · Period: **12.05.2026 – 17.07.2026** · Guide: Ms. A. Lakshmi, Manager

## Files

| File | What it is |
|---|---|
| `Lingesh K - SIP Report 2026.docx` | **The submission copy.** Open in Word, insert the certificate scan, export to PDF. |
| `SIP-Report-2026.md` | Same text in Markdown, for reading/reviewing on GitHub. |
| `Internship Certificate.png` | Scan of the internship completion certificate, embedded in the report. |
| `Aarti Chettiar-SIP Report .pdf` | Senior's report, used only as a reference for structure and formatting. |
| `tools/report_content.py` | All report text lives here — edit this to change any wording. |
| `tools/build_report.py` | Renders the content into the `.docx` and `.md`. |
| `tools/docx_writer.py` | Minimal OOXML writer (no external packages needed). |
| `tools/verify_docx.py` | Structural check of the generated `.docx`. |

## Rebuilding after an edit

```sh
python3 tools/build_report.py
python3 tools/verify_docx.py "Lingesh K - SIP Report 2026.docx"
```

## The internship certificate

`Internship Certificate.png` is embedded automatically on the INTERNSHIP CERTIFICATE page,
scaled to 6.02" × 8.02" so it fills the page under the heading. To swap in a better scan,
either overwrite that file or drop it at `assets/internship-certificate.png` (which takes
precedence) and rebuild.

## Notes on the document

- A4, Times New Roman 12 pt, 1.5 line spacing, justified; 1" margins with 1.25" on the
  binding edge.
- Front matter is unnumbered; page numbering restarts at 1 from Chapter 1, shown in the
  running header along with the chapter name.
- The page numbers in the Table of Contents are Word `PAGEREF` fields, so they update
  themselves. If they show stale values, press `Ctrl+A` then `F9` in Word.
