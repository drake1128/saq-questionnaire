"""Extract slides from PowerPoint / PDF source files into per-page PNGs.

Pipeline:
  .ppt / .pptx / .pptm  --(PowerPoint COM SaveAs PDF)-->  .pdf  --(PyMuPDF)-->  .png pages
  .pdf                                                       --(PyMuPDF)-->  .png pages

Usage (CLI):
  python extract_slides.py <input_file> <output_dir> [--dpi 300]
"""
from __future__ import annotations

import argparse
import sys
import tempfile
from pathlib import Path

import fitz  # PyMuPDF

PPT_EXTS = {'.ppt', '.pptx', '.pptm'}
PDF_EXTS = {'.pdf'}

def _ppt_to_pdf(src: Path, tmp_dir: Path) -> Path:
    """Convert a PowerPoint-family file to PDF via PowerPoint COM on Windows."""
    if sys.platform != 'win32':
        raise RuntimeError('PowerPoint COM only supported on Windows. '
                           'For non-Windows, install LibreOffice and switch to soffice.')
    import win32com.client
    out = tmp_dir / (src.stem + '.pdf')
    ppt_app = win32com.client.Dispatch('PowerPoint.Application')
    # Note: Some PowerPoint installs require Visible=True.
    try:
        pres = ppt_app.Presentations.Open(str(src.resolve()), WithWindow=False)
        # 32 = ppSaveAsPDF in PowerPoint FileFormat enum
        pres.SaveAs(str(out.resolve()), 32)
        pres.Close()
    finally:
        ppt_app.Quit()
    return out

def _pdf_to_pngs(pdf_path: Path, out_dir: Path, dpi: int = 300) -> list[Path]:
    """Render each PDF page to a PNG in out_dir."""
    out_dir.mkdir(parents=True, exist_ok=True)
    doc = fitz.open(str(pdf_path))
    zoom = dpi / 72.0
    mat = fitz.Matrix(zoom, zoom)
    paths: list[Path] = []
    for i, page in enumerate(doc, start=1):
        pix = page.get_pixmap(matrix=mat, alpha=False)
        out_file = out_dir / f'slide-{i:03d}.png'
        pix.save(str(out_file))
        paths.append(out_file)
    doc.close()
    return paths

def extract(src: Path, out_dir: Path, dpi: int = 300) -> list[Path]:
    """Extract slides from `src` (ppt-family or pdf) to `out_dir`.

    Returns sorted list of generated PNG paths.
    """
    src = Path(src)
    out_dir = Path(out_dir)
    suffix = src.suffix.lower()
    if suffix in PPT_EXTS:
        with tempfile.TemporaryDirectory() as td:
            pdf = _ppt_to_pdf(src, Path(td))
            return _pdf_to_pngs(pdf, out_dir, dpi=dpi)
    if suffix in PDF_EXTS:
        return _pdf_to_pngs(src, out_dir, dpi=dpi)
    raise ValueError(f'Unsupported file type: {suffix}')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input')
    parser.add_argument('output_dir')
    parser.add_argument('--dpi', type=int, default=300)
    args = parser.parse_args()
    paths = extract(Path(args.input), Path(args.output_dir), dpi=args.dpi)
    print(f'Extracted {len(paths)} pages.')
    for p in paths:
        print(' ', p)

if __name__ == '__main__':
    main()
