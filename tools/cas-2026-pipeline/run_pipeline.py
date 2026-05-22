"""Run the full image extraction + sidecar generation pipeline for all 9 chapters."""
from __future__ import annotations

import json
import sys
from pathlib import Path

import extract_slides
import generate_sidecar

SOURCE_DIR = Path(r"G:\我的雲端硬碟\004 教學資料 at Hsinchu 院內\Carotid 頸動脈支架訓練課程歷年投影片 2026")
REPO_ROOT = Path(__file__).resolve().parent.parent.parent
SIDECAR_DIR = REPO_ROOT / 'docs' / 'cas-2026'

def main(dpi: int = 200):
    sources_path = Path(__file__).parent / 'chapter_sources.json'
    chapter_sources = json.loads(sources_path.read_text(encoding='utf-8'))

    for chapter_id, sources_meta in chapter_sources.items():
        print(f'\n=== {chapter_id} ===')
        for s in sources_meta:
            src_file = SOURCE_DIR / s['file']
            out_dir  = SIDECAR_DIR / chapter_id / f'{s["year"]}-{s["slug"]}'
            if not src_file.exists():
                print(f'  SKIP missing source: {src_file.name}')
                continue
            if out_dir.exists() and any(out_dir.glob('slide-*.png')):
                print(f'  SKIP already extracted: {out_dir.name}')
                continue
            print(f'  Extracting {src_file.name} -> {out_dir.name}')
            try:
                paths = extract_slides.extract(src_file, out_dir, dpi=dpi)
                print(f'    {len(paths)} slides')
            except Exception as e:
                print(f'  ERROR extracting {src_file.name}: {e}')

    print('\n--- Generating sidecar HTMLs ---')
    generate_sidecar.main()

if __name__ == '__main__':
    dpi = int(sys.argv[1]) if len(sys.argv) > 1 else 200
    main(dpi=dpi)
