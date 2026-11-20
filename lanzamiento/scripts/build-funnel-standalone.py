#!/usr/bin/env python3
"""Genera funnel-standalone.html: el funnel en un solo archivo (fuentes y artes incrustados) para abrirlo en local.
Uso: python3 lanzamiento/scripts/build-funnel-standalone.py"""
import base64, io, json, re, pathlib
from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parent.parent
src = (ROOT / 'funnel.html').read_text(encoding='utf-8')

def data_uri(path, mime):
    return f"data:{mime};base64,{base64.b64encode(path.read_bytes()).decode()}"

# Fuentes
for m in set(re.findall(r'url\("(lz/fonts/[^"]+)"\)', src)):
    mime = 'font/otf' if m.endswith('.otf') else 'font/ttf'
    src = src.replace(f'url("{m}")', f'url("{data_uri(ROOT / m, mime)}")')

# Artes: JPEG comprimido, máx. 1400 px por lado
pieces = {}
for f in sorted((ROOT / 'artes' / 'piezas').glob('*.png')):
    im = Image.open(f).convert('RGB')
    im.thumbnail((1400, 1400))
    buf = io.BytesIO(); im.save(buf, 'JPEG', quality=84, optimize=True, progressive=True)
    pieces[f.name] = 'data:image/jpeg;base64,' + base64.b64encode(buf.getvalue()).decode()

inject = f'<script>window.PIECES = {json.dumps(pieces)};</script>\n<script>\n// ---------- Datos'
assert '<script>\n// ---------- Datos' in src
src = src.replace('<script>\n// ---------- Datos', inject, 1)
out = ROOT / 'funnel-standalone.html'
out.write_text(src, encoding='utf-8')
print(out, f'{out.stat().st_size/1e6:.1f} MB', len(pieces), 'artes')
