"""Generate sidecar slide-overview HTMLs (one per chapter) for user review."""
from __future__ import annotations

import json
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

CHAPTER_TITLES = {
    '01-ultrasound':  'Ch1 Ultrasound Diagnosis',
    '02-ct-mr':       'Ch2 CT / MR for ICAS',
    '03-occlusion':   'Ch3 Stenosis & Occlusion',
    '04-techniques':  'Ch4 General CAS Techniques',
    '05-epd':         'Ch5 Embolic Protection Device',
    '06-stent-design':'Ch6 Stent Design & TTT',
    '07-tsci':        'Ch7 Carotid TSCI',
    '08-surgical':    'Ch8 Surgical Approaches',
    '09-difficult':   'Ch9 Difficult CAS Tips & Tricks',
}

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
SIDECAR_DIR = REPO_ROOT / 'docs' / 'cas-2026'
EXTRACTED_ROOT = SIDECAR_DIR  # PNGs live under docs/cas-2026/<chapter>/<year>-<slug>/

def list_slides(folder: Path):
    if not folder.exists():
        return []
    pngs = sorted(folder.glob('slide-*.png'))
    return [
        {
            'seq': int(p.stem.split('-')[1]),
            'rel_path': p.relative_to(SIDECAR_DIR).as_posix(),
        }
        for p in pngs
    ]

def generate_for_chapter(chapter_id: str, sources_meta: list[dict]) -> Path:
    env = Environment(loader=FileSystemLoader(Path(__file__).parent), autoescape=True)
    tmpl = env.get_template('sidecar_template.html.j2')

    sources = []
    for s in sources_meta:
        folder = SIDECAR_DIR / chapter_id / f'{s["year"]}-{s["slug"]}'
        slides = list_slides(folder)
        sources.append({
            'year': s['year'],
            'speaker': s['speaker'],
            'slug': s['slug'],
            'slides': slides,
        })

    out_path = SIDECAR_DIR / f'{chapter_id}-slides-overview.html'
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(
        tmpl.render(
            chapter_id=chapter_id,
            chapter_title=CHAPTER_TITLES[chapter_id],
            sources=sources,
        ),
        encoding='utf-8',
    )
    return out_path

def main():
    sources_path = Path(__file__).parent / 'chapter_sources.json'
    chapter_sources = json.loads(sources_path.read_text(encoding='utf-8'))
    for chapter_id, sources_meta in chapter_sources.items():
        out = generate_for_chapter(chapter_id, sources_meta)
        slide_count = sum(
            len(list_slides(SIDECAR_DIR / chapter_id / f'{s["year"]}-{s["slug"]}'))
            for s in sources_meta
        )
        print(f'  Generated {out.name} ({slide_count} slides)')

if __name__ == '__main__':
    main()
