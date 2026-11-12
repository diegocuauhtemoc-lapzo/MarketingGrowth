#!/usr/bin/env python3
"""Convierte cada página del kit en un HTML autocontenido (CSS, JS, fuentes e imágenes incrustados) para
publicarla como artifact propio y poder abrirla en una pestaña aparte.

Uso:
  python3 lanzamiento/scripts/build-standalone.py OUT_DIR [links.json]

links.json (opcional) mapea páginas del kit a su URL publicada, p. ej. {"reclutamiento.html": "https://claude.ai/artifact/..."},
para que los enlaces entre páginas sigan funcionando fuera del visor."""
import base64, json, mimetypes, pathlib, re, subprocess, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent          # lanzamiento/
OUT = pathlib.Path(sys.argv[1]); OUT.mkdir(parents=True, exist_ok=True)
LINKS = json.loads(pathlib.Path(sys.argv[2]).read_text()) if len(sys.argv) > 2 else {}
MIME = {'.otf': 'font/otf', '.ttf': 'font/ttf', '.woff2': 'font/woff2', '.svg': 'image/svg+xml', '.webp': 'image/webp',
        '.png': 'image/png', '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg'}
ASSET = re.compile(r'\.(otf|ttf|woff2|svg|webp|png|jpe?g)$', re.I)

def uri(path):
    return f"data:{MIME.get(path.suffix.lower(), mimetypes.guess_type(path.name)[0])};base64,{base64.b64encode(path.read_bytes()).decode()}"

def inline_css(css, base):
    def rep(m):
        ref = m.group(2)
        if ref.startswith(('data:', 'http', '#')): return m.group(0)
        p = (base / ref).resolve()
        if not p.exists(): p = (base / 'lz' / ref).resolve()   # variables CSS que se usan desde lz/lz-landing.css
        return f'url("{uri(p)}")' if p.exists() else m.group(0)
    return re.sub(r'url\((["\']?)([^)"\']+)\1\)', rep, css)

def build_html(name, out_name=None, force_fase=None):
    src = ROOT / name; base = src.parent
    html = src.read_text(encoding='utf-8')
    # Hojas de estilo
    def css(m):
        p = (base / m.group(1)).resolve()
        return f'<style>\n{inline_css(p.read_text(encoding="utf-8"), p.parent)}\n</style>'
    html = re.sub(r'<link rel="stylesheet" href="([^"]+)">', css, html)
    # Scripts externos
    html = re.sub(r'<script src="([^"]+)"></script>',
                  lambda m: f'<script>\n{(base / m.group(1)).read_text(encoding="utf-8")}\n</script>', html)
    # url() dentro de <style> y atributos style
    html = inline_css(html, base)
    # Cualquier cadena entre comillas que sea un archivo del kit (src="...", rutas en JS)
    def q(m):
        ref = m.group(2)
        if ASSET.search(ref) and not ref.startswith(('data:', 'http')):
            p = (base / ref).resolve()
            if p.exists(): return m.group(1) + uri(p) + m.group(1)
        return m.group(0)
    html = re.sub(r'(["\'])([^"\'<>\s]+)\1', q, html)
    # Enlaces entre páginas del kit
    for page, url in LINKS.items():
        html = html.replace(f'href="{page}"', f'href="{url}" target="_top"')
    if force_fase:
        html = html.replace('<head>', f'<head>\n<script>window.FORCE_FASE = "{force_fase}";</script>', 1)
    out = OUT / (out_name or name.replace('/', '-'))
    out.write_text(html, encoding='utf-8')
    return out

MD_CSS = """
body{margin:0;background:#fff;color:#3F3F46;font-family:Poppins,Arial,sans-serif}
article{max-width:900px;margin:0 auto;padding:40px 32px 80px}
h1,h2,h3{font-family:"Degular Display","Poppins",Arial,sans-serif;color:#240C50}
h1{font-size:36px;margin:0 0 16px}h2{font-size:24px;margin:40px 0 12px;padding-top:20px;border-top:1px solid #EFF0F6}h3{font-size:18px;margin:24px 0 8px}
p,li{font-size:15px;line-height:1.65}a{color:#8B55FE}
table{border-collapse:collapse;width:100%;font-size:13.5px;margin:12px 0 18px;display:block;overflow-x:auto}
th{background:#F5F2FF;color:#240C50;text-align:left}th,td{border:1px solid #E2E2E8;padding:8px 10px;vertical-align:top}
blockquote{margin:14px 0;padding:10px 16px;border-left:3px solid #8B55FE;background:#F5F2FF;border-radius:0 10px 10px 0;color:#5029A3}
code{background:#F0EEEE;padding:1px 6px;border-radius:6px;font-size:13px}
pre{background:#14142A;color:#DDD4FF;padding:16px;border-radius:12px;overflow-x:auto;font-size:12.5px;white-space:pre-wrap}pre code{background:none;padding:0}
hr{border:none;border-top:1px solid #EFF0F6;margin:24px 0}hr+h2{border-top:none;padding-top:0;margin-top:8px}
@media(max-width:640px){article{padding:24px 16px 60px}h1{font-size:28px}}
"""

def build_md(name, title):
    src = ROOT / name
    body = subprocess.run(['node', '-e', "const {marked}=require(process.argv[1]);let s='';process.stdin.on('data',d=>s+=d).on('end',()=>process.stdout.write(marked.parse(s)))",
                           str(ROOT / 'vendor' / 'marked.min.js')], input=src.read_text(encoding='utf-8'), capture_output=True, text=True, check=True).stdout
    for page, url in LINKS.items():
        body = body.replace(f'href="{page}"', f'href="{url}" target="_top"')
    ds = ROOT.parent / 'design-system'
    faces = re.findall(r'@font-face\s*{[^}]*(?:Poppins-(?:Regular|Medium|SemiBold)|DegularDisplay-Bold)\.[^}]*}', (ds / 'colors_and_type.css').read_text(encoding='utf-8'))
    fonts = inline_css('\n'.join(faces), ds)
    html = f'<!doctype html>\n<html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">' \
           f'<title>{title}</title><style>{fonts}{MD_CSS}</style></head><body><article>{body}</article></body></html>'
    out = OUT / (name.replace('/', '-').replace('.md', '.html'))
    out.write_text(html, encoding='utf-8')
    return out

if __name__ == '__main__':
    outs = [build_html('deck.html'), build_html('reloj-checador.html'), build_html('reloj-checador.html', 'reloj-checador-5-ene.html', 'post'),
            build_html('gestion-personal.html'), build_html('reclutamiento.html'),
            build_md('estrategia.md', 'Estrategia de lanzamiento'), build_md('copys.md', 'Copys y artes'),
            build_md('artes/claude-design.md', 'Artes con Claude Design')]
    for o in outs: print(f'{o.stat().st_size/1e6:5.1f} MB  {o.name}')
