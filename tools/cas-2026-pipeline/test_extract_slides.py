"""Tests for slide extraction.

Note: These tests require sample input files. The "smoke test" uses an actual
2022 source file to verify end-to-end behavior.
"""
import os
import shutil
import tempfile
import unittest
from pathlib import Path

import extract_slides as es

SOURCE_DIR = Path(r"G:\我的雲端硬碟\004 教學資料 at Hsinchu 院內\Carotid 頸動脈支架訓練課程歷年投影片 2026")
SAMPLE_PPTX = SOURCE_DIR / "2022年_05_黃成偉醫師_Embolic protection device.pptx"
SAMPLE_PDF  = SOURCE_DIR / "2024年_06_黃成偉醫師_Embolic protection device.pdf"

class TestExtract(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix='cas2026_test_'))

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_extract_pptx_produces_pngs(self):
        if not SAMPLE_PPTX.exists():
            self.skipTest(f'Sample missing: {SAMPLE_PPTX}')
        out = es.extract(SAMPLE_PPTX, self.tmp, dpi=150)  # lower DPI for test speed
        self.assertGreater(len(out), 0, 'no PNGs produced')
        for p in out:
            self.assertTrue(p.exists())
            self.assertEqual(p.suffix, '.png')
            self.assertGreater(p.stat().st_size, 1000, f'tiny file: {p}')

    def test_extract_pdf_produces_pngs(self):
        if not SAMPLE_PDF.exists():
            self.skipTest(f'Sample missing: {SAMPLE_PDF}')
        out = es.extract(SAMPLE_PDF, self.tmp, dpi=150)
        self.assertGreater(len(out), 0)

if __name__ == '__main__':
    unittest.main()
