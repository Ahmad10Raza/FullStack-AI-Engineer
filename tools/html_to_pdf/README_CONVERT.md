# Convert HTML to PDF

This folder contains a small CLI script to convert HTML files to PDF.

Files:
- `convert_html_to_pdf.py` — CLI script. Usage: `python tools/convert_html_to_pdf.py input.html output.pdf [--backend wkhtml|playwright]`
- `requirements.txt` — Python packages used by the script.

Recommended (simple) backend — wkhtmltopdf

1. Install system binary:

Debian/Ubuntu:

    sudo apt-get update && sudo apt-get install -y wkhtmltopdf

macOS (Homebrew):

    brew install wkhtmltopdf

Or download a release from https://wkhtmltopdf.org/

2. Create a virtualenv and install Python deps:

    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r tools/requirements.txt

3. Run:

    python tools/convert_html_to_pdf.py python.html python.pdf --backend wkhtml

Playwright backend (better for JS-heavy pages)

1. Install Python deps and browsers:

    pip install playwright
    python -m playwright install

2. Run with backend `playwright`:

    python tools/convert_html_to_pdf.py python.html python_playwright.pdf --backend playwright

Notes
- The script defaults to `python.html` -> `python.pdf` when no args are supplied.
- If your HTML references local assets (CSS, images), both backends support local file access, but make sure the HTML uses relative paths or `file://` URIs.
