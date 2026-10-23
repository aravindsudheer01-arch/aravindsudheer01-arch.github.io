# Website verification — 23 October 2026

## Completed checks

| Check | Result |
|---|---|
| Static build | 17 HTML pages; 10 case studies generated successfully |
| Offline structural/link check | 390 local references checked; zero errors |
| Build/content unit tests | 10 passed |
| New-project workflow | Temporary draft excluded, then published after setting `draft: false`; generated links checked; temporary content removed |
| Local HTTP requests | 23 requests: 17 HTML pages, CSS, JavaScript and four CV PDFs; all HTTP 200 with content |
| Chromium layout checks | 17 pages × 4 viewport widths = 68 rendered-page checks |
| Widths | 320, 390, 768 and 1440 CSS pixels |
| Layout/runtime issues | No horizontal overflow, JavaScript errors or failed embedded asset requests in those checks |
| Interactions | Category filter, keyword search, empty-state reset, mobile menu, Escape dismissal and closing on contact navigation passed |
| Progressive enhancement | Content and navigation usable without JavaScript; reduced-motion preference respected |
| CV output | All four PDFs are one page, contain a clickable GitHub URL and omit the phone number |
| Visual inspection | Desktop homepage, work index, solar case study, mobile layout and all four CV pages reviewed |

## Method and important limits

The build, unit tests and local HTTP requests ran against the actual delivered files. The browser environment blocked direct navigation to both localhost and `file://` URLs. No browser policy was changed. For layout and interaction checks, Chromium rendered the generated HTML with local CSS, JavaScript and images embedded into the page. The QA harness made images eager-loading for capture; the production site retains native image loading behavior.

This verifies the rendered layout and the tested client-side interactions, but **is not a hosted end-to-end test**. Actual resource delivery was checked separately through Python HTTP requests to the local preview server. The report does not claim browser PDF-download network requests, live secure-context clipboard writes, Safari or physical-device testing. External project applications were not executed during the website build.

The build used the declared package versions available in this environment. A fresh dependency installation and the GitHub Actions deployment have not been executed here. The workflow is supplied for deployment in your account; no remote repository was created or changed.

## Reproduce the checks

```bash
python build.py
python -m unittest discover -s tests -v
python scripts/check_site.py
python serve.py
```

Then use your browser at `http://127.0.0.1:8000`, check a mobile-width layout, search/filter the work page, open case studies and download all four PDFs. After deployment, repeat these checks using the live HTTPS URL, including email copying.

## Raw observations

- `browser-report.json`: per-page viewports, interaction results and untested conditions.
- `http-report.json`: actual local paths, response status, size and content type.
- `cv-report.json`: PDF page count, hyperlink and phone omission checks.

No performance score, cross-browser certification or accessibility-conformance certification is claimed.
