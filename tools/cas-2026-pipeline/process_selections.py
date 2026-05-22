"""Read user-exported selection JSONs and copy chosen PNGs to images-cas-2026/."""
from __future__ import annotations

import json
import shutil
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
SIDECAR_DIR = REPO_ROOT / 'docs' / 'cas-2026'
IMAGES_ROOT = REPO_ROOT / 'images-cas-2026'
SELECTIONS_DIR = Path(__file__).parent / 'selections'

def process_one(selection_file: Path):
    data = json.loads(selection_file.read_text(encoding='utf-8'))
    chapter_id = data['chapter']  # e.g. '05-epd'
    chapter_imgs = IMAGES_ROOT / chapter_id
    chapter_imgs.mkdir(parents=True, exist_ok=True)
    copied = []
    for entry in data['selected']:
        source = entry['source']      # e.g. '2022-huang-cw'
        seq = entry['seq']            # int
        src_png = SIDECAR_DIR / chapter_id / source / f'slide-{seq:03d}.png'
        if not src_png.exists():
            print(f'  MISSING {src_png}')
            continue
        dst_png = chapter_imgs / f'{source}-seq{seq:03d}.png'
        shutil.copy2(src_png, dst_png)
        copied.append(dst_png)
    print(f'  {chapter_id}: copied {len(copied)} images')
    return copied

def main():
    if not SELECTIONS_DIR.exists():
        raise SystemExit(f'No selections directory: {SELECTIONS_DIR}')
    sel_files = sorted(SELECTIONS_DIR.glob('cas-2026-*-selection.json'))
    if not sel_files:
        raise SystemExit('No selection JSON files found.')
    for sf in sel_files:
        print(f'Processing {sf.name}')
        process_one(sf)

if __name__ == '__main__':
    main()
