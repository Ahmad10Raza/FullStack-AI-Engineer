#!/usr/bin/env python3
"""Convert an HTML file to PDF.

Primary backend: wkhtmltopdf via pdfkit (fast and good for static HTML/CSS).
Fallback backend: Playwright (full browser rendering for JS-heavy pages).

Usage:
  python tools/convert_html_to_pdf.py input.html output.pdf [--backend wkhtml|playwright]

See README_CONVERT.md for installation notes.
"""
from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path


def convert_with_pdfkit(input_path: Path, output_path: Path) -> None:
    try:
        import pdfkit
    except ImportError:
        raise RuntimeError("pdfkit is not installed. Run: pip install pdfkit")

    wk = shutil.which("wkhtmltopdf")
    if not wk:
        raise RuntimeError(
            "wkhtmltopdf binary not found. Install it (apt, brew or download from https://wkhtmltopdf.org/)."
        )

    config = pdfkit.configuration(wkhtmltopdf=wk)
    options = {
        "enable-local-file-access": None,  # Allow relative/local file assets
        "margin-top": "12mm",
        "margin-bottom": "12mm",
        "margin-left": "10mm",
        "margin-right": "10mm",
        "page-size": "A4",
    }

    # pdfkit accepts str paths
    pdfkit.from_file(str(input_path), str(output_path), configuration=config, options=options)


def convert_with_playwright(input_path: Path, output_path: Path) -> None:
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        raise RuntimeError("playwright is not installed. Run: pip install playwright and python -m playwright install")

    html_url = input_path.resolve().as_uri()

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(html_url, wait_until="networkidle")
        # print to pdf with default A4 layout; adjust as needed
        page.pdf(path=str(output_path), format="A4", margin={"top": "12mm", "bottom": "12mm", "left": "10mm", "right": "10mm"})
        browser.close()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Convert HTML to PDF")
    parser.add_argument("input", nargs="?", default="python.html", help="Input HTML file path")
    parser.add_argument("output", nargs="?", default="python.pdf", help="Output PDF file path")
    parser.add_argument(
        "--backend",
        choices=("wkhtml", "playwright"),
        default="wkhtml",
        help="Rendering backend to use (wkhtml: pdfkit + wkhtmltopdf; playwright: headless Chromium)",
    )

    args = parser.parse_args(argv)
    input_path = Path(args.input)
    output_path = Path(args.output)

    if not input_path.exists():
        print(f"Input file not found: {input_path}")
        return 2

    try:
        if args.backend == "wkhtml":
            convert_with_pdfkit(input_path, output_path)
        else:
            convert_with_playwright(input_path, output_path)
    except Exception as e:
        print(f"Conversion failed: {e}")
        return 1

    print(f"Wrote PDF: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
