#!/usr/bin/env python3
"""Arma la página única del lanzamiento: presentación, estrategia, funnel, copys y artes, y landing pages,
todo en un solo HTML autocontenido.

Uso: python3 lanzamiento/scripts/build-suite.py SALIDA.html"""
import base64, html, importlib.util, io, json, pathlib, re, sys
from PIL import Image

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
spec = importlib.util.spec_from_file_location('sa', HERE / 'build-standalone.py'); sa = importlib.util.module_from_spec(spec); spec.loader.exec_module(sa)

def b64(path, mime):
    return f'data:{mime};base64,{base64.b64encode(path.read_bytes()).decode()}'

def jpeg(path, max_side=1400, q=82):
    im = Image.open(path).convert('RGB'); im.thumbnail((max_side, max_side))
    buf = io.BytesIO(); im.save(buf, 'JPEG', quality=q, optimize=True, progressive=True)
    return 'data:image/jpeg;base64,' + base64.b64encode(buf.getvalue()).decode()

# ---------- Documentos incrustados (iframes srcdoc, se cargan al abrir la pestaña) ----------
sa.FONT_KEEP = r'DegularDisplay-(Bold|Semibold)\.|Poppins-(Regular|Medium|SemiBold|Bold|Italic)\.'
deck = sa.build_html('deck.html')
funnel = (ROOT / 'funnel.html').read_text(encoding='utf-8')
funnel = sa.inline_css(funnel, ROOT)
# El funnel toma las imágenes de los artes de la página principal (mismo origen), sin duplicarlas.
funnel = funnel.replace('<script>\n// ---------- Datos', '<script>try { window.PIECES = parent.SUITE_PIECES; } catch (e) {}</script>\n<script>\n// ---------- Datos', 1)
funnel = funnel.replace("link:'reloj-checador.html'", "link:'#landings'")

# ---------- Artes ----------
PIECES_DIR = ROOT / 'artes' / 'piezas'
pieces = {f.name: jpeg(f) for f in sorted(PIECES_DIR.glob('*.png'))}
LOTE1 = [
    ('li-webinar-ley-1200x627.png', 'LinkedIn · 1200×627', 'El 1 de enero el registro de jornada deja de ser opcional'),
    ('li-webinar-horas-extra-1200x627.png', 'LinkedIn · 1200×627', 'Las horas extra que no registras son un riesgo'),
    ('li-webinar-ley-1080x1080.png', 'LinkedIn · 1080×1080', 'El 1 de enero el registro de jornada deja de ser opcional'),
    ('li-reloj-pedro-a-1200x627.png', 'LinkedIn · 1200×627 · Pedro Sors', 'Prepara a tu empresa para el Reloj Checador'),
    ('li-reloj-pedro-b-1200x627.png', 'LinkedIn · 1200×627 · Pedro Sors', 'Tu empresa, lista para el Reloj Checador'),
    ('li-reloj-pedro-c-1200x627.png', 'LinkedIn · 1200×627 · Pedro Sors', 'El Reloj Checador llega el 31 de diciembre'),
    ('li-reloj-pedro-d-1200x627.png', 'LinkedIn · 1200×627 · Pedro Sors', 'Llega al 1 de enero con tu Reloj Checador listo'),
    ('meta-webinar-excel-1080x1080.png', 'Meta · 1080×1080', '¿Todavía registras asistencias en Excel?'),
    ('meta-webinar-agenda-1080x1350.png', 'Meta · 1080×1350', 'Lo que tu empresa debe tener listo el 1 de enero'),
    ('meta-webinar-story-1080x1920.png', 'Meta · Story 1080×1920', 'El registro de jornada ya tiene fecha'),
]
PENDING = [
    ('Lote 2 · 16 nov', 'Anuncio de los tres productos', '1200×627 · 1080×1080 · 1080×1350'),
    ('Lote 2 · 16 nov', 'Headers de email (tres productos, webinar, Reloj Checador)', '600×200'),
    ('Lote 3 · desde 25 nov', 'Preventa: primera ola de enero', '1080×1080 · 1200×627'),
    ('Lote 3 · 2, 18 y 25 dic', 'Cuenta regresiva: 30, 14 y 7 días', '1080×1080'),
    ('Lote 3 · diciembre', 'Carrusel "Qué cambia el 1 de enero"', '1080×1350 × 6'),
    ('Lote 3 · 5 ene', 'Reloj Checador ya está aquí', '1080×1080 · 1200×627 · 1080×1920'),
]

# ---------- Landings (capturas de escritorio y móvil) ----------
MOCK = ROOT / 'artes' / 'mockups'
LANDINGS = [
    ('reloj', 'Reloj Checador', 'Preventa', 'lapzo.co/reloj-checador', 'Hasta el 4 de enero. Lista prioritaria, webinar del 24 de noviembre y cuenta regresiva al 1 de enero. El hero muestra el widget de Control Horario en sus estados.'),
    ('reloj-5ene', 'Reloj Checador', 'Lanzamiento', 'lapzo.co/reloj-checador', 'Desde el 5 de enero. La página cambia sola: "Agenda tu habilitación", sin webinar y con el producto disponible.'),
    ('gp', 'Gestión de Personal', 'Disponible', 'lapzo.co/gestion-de-personal', 'Organigrama, expediente, solicitudes con aprobación y documentos. Llamado a la acción: agenda una demo.'),
    ('rec', 'Reclutamiento', 'Disponible', 'lapzo.co/reclutamiento', 'Vacantes por competencias e IAMatch, con vacantes y postulantes ilimitados. Llamado a la acción: agenda una demo.'),
]
mock = {k: {'desk': b64(MOCK / f'{k}-desk.jpg', 'image/jpeg'), 'mob': b64(MOCK / f'{k}-mob.jpg', 'image/jpeg')} for k, *_ in LANDINGS}

# ---------- Markdown ----------
def md(name):
    t = (ROOT / name).read_text(encoding='utf-8')
    out = sa.md_to_html(t)
    # ids para el índice
    seen = {}
    def hid(m):
        txt = re.sub('<[^>]+>', '', m.group(2)); slug = re.sub(r'[^a-z0-9]+', '-', txt.lower().translate(str.maketrans('áéíóúñü', 'aeiounu'))).strip('-')[:48]
        seen[slug] = seen.get(slug, 0) + 1; slug += '' if seen[slug] == 1 else f'-{seen[slug]}'
        return f'<h{m.group(1)} id="{name.split("/")[-1].split(".")[0]}-{slug}">{m.group(2)}</h{m.group(1)}>'
    out = re.sub(r'<h([23])>(.*?)</h\1>', hid, out)
    toc = re.findall(r'<h2 id="([^"]+)">(.*?)</h2>', out)
    return out, [(i, re.sub('<[^>]+>', '', t)) for i, t in toc]

estr, estr_toc = md('estrategia.md')
copys, copys_toc = md('copys.md')
guia, _ = md('artes/claude-design.md')

font = lambda f: b64(ROOT / 'lz' / 'fonts' / f, 'font/otf' if f.endswith('.otf') else 'font/ttf')
FONTS = f"""
@font-face{{font-family:"Poppins";src:url({font('Poppins-Regular.ttf')}) format("truetype");font-weight:400;font-display:swap}}
@font-face{{font-family:"Poppins";src:url({font('Poppins-Medium.ttf')}) format("truetype");font-weight:500;font-display:swap}}
@font-face{{font-family:"Poppins";src:url({font('Poppins-SemiBold.ttf')}) format("truetype");font-weight:600;font-display:swap}}
@font-face{{font-family:"LZ Degular";src:url({font('Degular-Bold.otf')}) format("opentype");font-weight:700;font-display:swap}}
@font-face{{font-family:"LZ Degular";src:url({font('Degular-Semibold.otf')}) format("opentype");font-weight:600;font-display:swap}}
"""
LOGO = b64(ROOT / 'lz' / 'lapzo-lockup-inverse.svg', 'image/svg+xml')

esc = lambda s: html.escape(s, quote=True)
toc_html = lambda toc: ''.join(f'<a href="#{i}" data-toc>{esc(t)}</a>' for i, t in toc)
gallery = ''.join(f'<figure class="art"><button type="button" class="art-btn" data-lb="{f}" aria-label="Ver {esc(t)} en grande"><img src="{pieces[f]}" alt="{esc(t)}" loading="lazy"></button><figcaption><span>{esc(fmt)}</span>{esc(t)}</figcaption></figure>' for f, fmt, t in LOTE1 if f in pieces)
pending = ''.join(f'<li><span class="chip">{esc(l)}</span><b>{esc(n)}</b><small>{esc(fmt)}</small></li>' for l, n, fmt in PENDING)
land_tabs = ''.join(f'<button type="button" class="seg" data-land="{k}" aria-pressed="false"><b>{esc(n)}</b><small>{esc(st)}</small></button>' for k, n, st, *_ in LANDINGS)
land_data = json.dumps({k: {'name': n, 'state': st, 'url': u, 'note': note, **mock[k]} for k, n, st, u, note in LANDINGS})

page = f"""<title>Lanzamiento Q4 2026</title>
<meta name="claude:viewport-fit-sides" content="cover">
<style>
{FONTS}
/* Marco de una sola página con pestañas: barra superior en tinta de lapzo.co, vistas a pantalla completa debajo. */
:root{{
  color-scheme:light;
  --ink:#211435; --ink-2:#2e1f48; --action:#7d4de5; --action-2:#5624c0; --hl:#c7a4ff; --brand-10:#ebecfe; --brand-30:#a996ff;
  --canvas:#f7f8f9; --surface:#ffffff; --text:#262338; --text-2:#4e4b66; --muted:#666983; --border:#d9dbe9; --line:#eff0f6;
  --warn-bg:#fff3cc; --warn:#7a5a00; --ok-bg:#eaf9de; --ok:#067306;
  --font:"Poppins",Arial,sans-serif; --display:"LZ Degular","Poppins",Arial,sans-serif;
  --bar-h:108px;
}}
*{{box-sizing:border-box}}
html,body{{height:100%}}
body{{margin:0;background:var(--canvas);color:var(--text);font:400 15px/1.55 var(--font);-webkit-font-smoothing:antialiased}}
body::before{{content:"";position:fixed;inset:0 0 auto;height:env(safe-area-inset-top,0px);z-index:60;background:var(--ink)}}
button{{font:inherit;color:inherit}}
:focus-visible{{outline:3px solid var(--brand-30);outline-offset:2px}}
.wrap{{padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}}

/* Barra superior */
.top{{position:sticky;top:env(safe-area-inset-top,0px);z-index:50;background:var(--ink);color:#fff;border-bottom:1px solid rgba(255,255,255,.08)}}
.top .row{{display:flex;align-items:center;gap:16px;padding-block:12px 8px}}
.top img{{height:24px;display:block}}
.top .ttl{{font:600 13px/1.3 var(--font);color:rgba(255,255,255,.72);border-left:1px solid rgba(255,255,255,.18);padding-left:16px}}
.top .ttl b{{display:block;color:#fff;font:700 18px/1.1 var(--display);letter-spacing:-.01em}}
.top .meta{{margin-left:auto;font:500 12px/1.3 var(--font);color:rgba(255,255,255,.6);text-align:right}}
.tabs{{display:flex;gap:4px;overflow-x:auto;scrollbar-width:none;padding-block:4px 10px}}
.tabs::-webkit-scrollbar{{display:none}}
.tab{{flex:0 0 auto;border:none;background:transparent;color:rgba(255,255,255,.72);font:500 14px/1 var(--font);padding:10px 14px;border-radius:10px;cursor:pointer;text-decoration:none}}
.tab:hover{{background:rgba(255,255,255,.07);color:#fff}}
.tab[aria-current="page"]{{background:var(--brand-30);color:var(--ink);font-weight:600}}

.view[hidden]{{display:none!important}}
.full{{height:calc(100dvh - var(--bar-h) - env(safe-area-inset-top,0px) - env(safe-area-inset-bottom,0px));min-height:520px;display:flex;flex-direction:column}}
.full iframe{{flex:1;width:100%;border:0;display:block;background:var(--surface)}}
.toolbar{{display:flex;align-items:center;gap:10px;flex-wrap:wrap;padding-block:10px;background:var(--surface);border-bottom:1px solid var(--line);font-size:13px;color:var(--muted)}}
.toolbar .sp{{flex:1}}
.btn{{display:inline-flex;align-items:center;gap:6px;border:1px solid var(--border);background:var(--surface);color:var(--text);border-radius:10px;padding:7px 12px;font:600 13px/1 var(--font);cursor:pointer}}
.btn:hover{{border-color:var(--action);color:var(--action-2)}}
.btn.primary{{background:var(--action);border-color:var(--action);color:#fff}}
.btn.primary:hover{{background:var(--action-2);color:#fff}}

/* Documentos */
.doc{{display:grid;grid-template-columns:minmax(0,240px) minmax(0,1fr);gap:40px;max-width:1240px;margin:0 auto;padding-block:32px 80px}}
.toc{{position:sticky;top:calc(var(--bar-h) + 20px);align-self:start;display:flex;flex-direction:column;gap:2px;max-height:calc(100dvh - var(--bar-h) - 40px);overflow:auto}}
.toc h4{{margin:0 0 8px;font:600 11px/1 var(--font);letter-spacing:.08em;text-transform:uppercase;color:var(--action)}}
.toc a{{color:var(--text-2);text-decoration:none;font-size:13px;line-height:1.35;padding:6px 10px;border-radius:8px}}
.toc a:hover{{background:var(--brand-10);color:var(--action-2)}}
article{{min-width:0;max-width:860px}}
article h1{{font:700 clamp(30px,4vw,44px)/1.05 var(--display);letter-spacing:-.015em;color:var(--ink);margin:0 0 16px;text-wrap:balance}}
article h2{{font:700 26px/1.15 var(--display);color:var(--ink);margin:44px 0 12px;padding-top:24px;border-top:1px solid var(--line);scroll-margin-top:calc(var(--bar-h) + 16px);text-wrap:balance}}
article h3{{font:600 17px/1.3 var(--font);color:var(--ink);margin:26px 0 8px;scroll-margin-top:calc(var(--bar-h) + 16px)}}
article p,article li{{color:var(--text-2);max-width:72ch}}
article a{{color:var(--action-2)}}
article table{{border-collapse:collapse;width:100%;font-size:13.5px;margin:12px 0 20px;display:block;overflow-x:auto}}
article th{{background:var(--brand-10);color:var(--ink);text-align:left;font-weight:600}}
article th,article td{{border:1px solid var(--border);padding:8px 10px;vertical-align:top}}
article blockquote{{margin:14px 0;padding:10px 16px;border-left:3px solid var(--action);background:var(--brand-10);border-radius:0 10px 10px 0}}
article blockquote p{{color:var(--action-2);margin:4px 0}}
article code{{background:var(--line);padding:1px 6px;border-radius:6px;font-size:13px}}
article pre{{background:var(--ink);color:#e9e2ff;padding:16px;border-radius:12px;overflow-x:auto;font-size:12.5px;white-space:pre-wrap}}
article pre code{{background:none;padding:0;color:inherit}}
article hr{{border:none;border-top:1px solid var(--line);margin:24px 0}}
article hr+h2{{border-top:none;padding-top:0;margin-top:8px}}

/* Copys y artes */
.sec-head{{display:flex;flex-direction:column;gap:6px;margin-bottom:20px}}
.kicker{{font:600 12px/1 var(--font);letter-spacing:.08em;text-transform:uppercase;color:var(--action)}}
.sec-head h2{{margin:0;font:700 clamp(26px,3.4vw,38px)/1.05 var(--display);color:var(--ink);letter-spacing:-.015em;text-wrap:balance}}
.sec-head p{{margin:0;color:var(--muted);max-width:70ch}}
.arts{{max-width:1240px;margin:0 auto;padding-block:32px 8px}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(min(100%,260px),1fr));gap:18px}}
.art{{margin:0;background:var(--surface);border:1px solid var(--line);border-radius:14px;overflow:hidden;display:flex;flex-direction:column}}
.art-btn{{border:none;padding:0;background:var(--ink);cursor:zoom-in;display:block;aspect-ratio:4/3;max-width:100%}}
.art-btn img{{width:100%;height:100%;object-fit:contain;display:block}}
.art figcaption{{padding:10px 12px 12px;font-size:13px;line-height:1.35;color:var(--text);display:flex;flex-direction:column;gap:3px}}
.art figcaption span{{font:600 11px/1 var(--font);letter-spacing:.04em;color:var(--muted);text-transform:uppercase}}
.pending{{list-style:none;padding:0;margin:22px 0 0;display:grid;grid-template-columns:repeat(auto-fill,minmax(min(100%,300px),1fr));gap:10px}}
.pending li{{display:flex;flex-direction:column;gap:4px;padding:12px 14px;border:1px dashed var(--border);border-radius:12px;background:var(--surface)}}
.pending small{{color:var(--muted)}}
.chip{{align-self:flex-start;font:600 11px/1 var(--font);padding:4px 8px;border-radius:999px;background:var(--warn-bg);color:var(--warn)}}
.subnav{{display:flex;gap:8px;flex-wrap:wrap;margin-top:28px}}
details.guide{{max-width:1240px;margin:0 auto 60px;background:var(--surface);border:1px solid var(--line);border-radius:14px}}
details.guide summary{{cursor:pointer;padding:16px 20px;font:600 15px/1.3 var(--font);color:var(--ink)}}
details.guide article{{padding:0 20px 20px;max-width:none}}

/* Landings */
.lands{{max-width:1280px;margin:0 auto;padding-block:32px 60px}}
.segs{{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:18px}}
.seg{{border:1px solid var(--border);background:var(--surface);border-radius:12px;padding:10px 14px;cursor:pointer;text-align:left;display:flex;flex-direction:column;gap:2px;line-height:1.2}}
.seg b{{font-weight:600;font-size:14px;color:var(--ink)}}
.seg small{{font-size:12px;color:var(--muted)}}
.seg[aria-pressed="true"]{{border-color:var(--action);background:var(--brand-10);box-shadow:0 0 0 2px rgba(125,77,229,.18)}}
.stage{{display:grid;grid-template-columns:minmax(0,1fr) 300px;gap:28px;align-items:start;background:linear-gradient(160deg,var(--ink),var(--ink-2));border-radius:24px;padding:28px}}
.browser{{background:var(--surface);border-radius:14px;overflow:hidden;box-shadow:0 30px 70px rgba(0,0,0,.45);min-width:0}}
.browser .chrome{{display:flex;align-items:center;gap:6px;padding:10px 12px;background:#eceef4;border-bottom:1px solid #dcdfe8}}
.browser .chrome i{{width:10px;height:10px;border-radius:50%;background:#c9ccd8;display:block}}
.browser .chrome span{{margin-left:10px;flex:1;background:#fff;border-radius:8px;padding:5px 10px;font-size:12px;color:var(--muted);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}}
.screen{{height:min(62vh,620px);overflow-y:auto;overflow-x:hidden;background:#fff}}
.screen img{{width:100%;display:block}}
.phone{{justify-self:center;width:280px;max-width:100%;border-radius:40px;background:#0c0c1a;padding:12px;box-shadow:0 30px 70px rgba(0,0,0,.5)}}
.phone .screen{{height:min(62vh,560px);border-radius:28px}}
.land-info{{display:flex;flex-wrap:wrap;gap:12px 24px;align-items:baseline;margin-top:16px;color:var(--text-2)}}
.land-info b{{font:700 22px/1.1 var(--display);color:var(--ink)}}
.land-info .chip{{background:var(--ok-bg);color:var(--ok)}}
.land-info .chip.pre{{background:var(--warn-bg);color:var(--warn)}}
.hint{{font-size:12.5px;color:var(--muted);margin-top:6px}}

/* Visor de imagen */
.lb{{position:fixed;inset:0;z-index:100;background:rgba(20,20,42,.9);display:flex;align-items:center;justify-content:center;flex-direction:column;gap:10px;padding:max(24px,env(safe-area-inset-top,0px)) max(16px,env(safe-area-inset-right,0px)) max(24px,env(safe-area-inset-bottom,0px)) max(16px,env(safe-area-inset-left,0px))}}
.lb[hidden]{{display:none}}
.lb img{{max-width:100%;max-height:calc(100dvh - 110px);border-radius:10px;box-shadow:0 30px 80px rgba(0,0,0,.5)}}
.lb p{{color:#fff;margin:0;font-size:13px;opacity:.85;text-align:center}}
.lb .x{{position:absolute;top:calc(14px + env(safe-area-inset-top,0px));right:calc(14px + env(safe-area-inset-right,0px));width:38px;height:38px;border-radius:10px;border:none;background:#fff;color:var(--ink);cursor:pointer;font-size:16px}}

@media (max-width:900px){{
  :root{{--bar-h:112px}}
  .top .meta{{display:none}}
  .doc{{grid-template-columns:minmax(0,1fr);gap:16px;padding-block:20px 60px}}
  .toc{{position:static;max-height:none;flex-direction:row;flex-wrap:wrap;gap:4px}}
  .toc h4{{width:100%}}
  .toc a{{background:var(--surface);border:1px solid var(--line)}}
  .stage{{grid-template-columns:minmax(0,1fr);padding:16px;border-radius:18px}}
  .phone{{width:240px}}
}}
@media (prefers-reduced-motion:reduce){{*{{scroll-behavior:auto!important;transition:none!important}}}}
</style>

<header class="top">
  <div class="wrap">
    <div class="row">
      <img src="{LOGO}" alt="Lapzo">
      <div class="ttl"><b>Lanzamiento Q4 2026</b>Reclutamiento · Gestión de Personal · Reloj Checador</div>
      <div class="meta">Marketing y Growth<br>Webinar 24 nov · Release Reloj 31 dic</div>
    </div>
    <nav class="tabs" aria-label="Secciones">
      <a class="tab" href="#presentacion" data-view="presentacion">Presentación</a>
      <a class="tab" href="#estrategia" data-view="estrategia">Estrategia</a>
      <a class="tab" href="#funnel" data-view="funnel">Funnel</a>
      <a class="tab" href="#copys" data-view="copys">Copys y artes</a>
      <a class="tab" href="#landings" data-view="landings">Landing pages</a>
    </nav>
  </div>
</header>

<main>
  <section class="view full" id="v-presentacion" aria-label="Presentación">
    <div class="toolbar wrap">
      <span>13 diapositivas · flechas del teclado o botones para avanzar</span><span class="sp"></span>
      <button type="button" class="btn" id="d-prev" aria-label="Diapositiva anterior">←</button>
      <button type="button" class="btn" id="d-next" aria-label="Diapositiva siguiente">→</button>
      <button type="button" class="btn primary" id="d-full">Pantalla completa</button>
    </div>
    <iframe id="f-deck" title="Presentación" allowfullscreen data-srcdoc="{esc(deck)}"></iframe>
  </section>

  <section class="view" id="v-estrategia" aria-label="Estrategia" hidden>
    <div class="doc wrap">
      <nav class="toc" aria-label="Índice de la estrategia"><h4>Estrategia</h4>{toc_html(estr_toc)}</nav>
      <article>{estr}</article>
    </div>
  </section>

  <section class="view full" id="v-funnel" aria-label="Funnel" hidden>
    <iframe id="f-funnel" title="Funnel semana a semana" data-srcdoc="{esc(funnel)}"></iframe>
  </section>

  <section class="view" id="v-copys" aria-label="Copys y artes" hidden>
    <div class="arts wrap">
      <div class="sec-head"><span class="kicker">Artes</span><h2>Lote 1: webinar del 24 de noviembre</h2><p>Diez piezas producidas en Claude Design para LinkedIn y Meta. Haz clic en una pieza para verla en tamaño completo.</p></div>
      <div class="grid">{gallery}</div>
      <div class="sec-head" style="margin-top:36px"><span class="kicker">Por producir</span><h2>Lotes 2 y 3</h2></div>
      <ul class="pending">{pending}</ul>
      <div class="subnav"><a class="btn" href="#copys-texto">Ir a los copys</a></div>
    </div>
    <div class="doc wrap" id="copys-texto">
      <nav class="toc" aria-label="Índice de copys"><h4>Copys</h4>{toc_html(copys_toc)}</nav>
      <article>{copys}</article>
    </div>
    <div class="wrap"><details class="guide"><summary>Guía para producir los artes en Claude Design</summary><article>{guia}</article></details></div>
  </section>

  <section class="view" id="v-landings" aria-label="Landing pages" hidden>
    <div class="lands wrap">
      <div class="sec-head"><span class="kicker">Landing pages</span><h2>Cómo se ven en escritorio y en móvil</h2><p>Capturas de las landings construidas con el design system de lapzo.co. Desplázate dentro de cada pantalla para recorrer la página completa.</p></div>
      <div class="segs" role="group" aria-label="Landing">{land_tabs}</div>
      <div class="stage">
        <div class="browser"><div class="chrome"><i></i><i></i><i></i><span id="l-url"></span></div><div class="screen" tabindex="0" aria-label="Vista de escritorio"><img id="l-desk" alt=""></div></div>
        <div class="phone"><div class="screen" tabindex="0" aria-label="Vista móvil"><img id="l-mob" alt=""></div></div>
      </div>
      <div class="land-info"><b id="l-name"></b><span class="chip" id="l-state"></span><span id="l-note"></span></div>
      <p class="hint">Los formularios se conectarán a HubSpot antes de publicar en lapzo.co.</p>
    </div>
  </section>
</main>

<div class="lb" id="lb" role="dialog" aria-modal="true" aria-label="Arte en tamaño completo" hidden><button type="button" class="x" aria-label="Cerrar">✕</button><img alt=""><p></p></div>

<script>
window.SUITE_PIECES = {json.dumps(pieces)};
const LANDS = {land_data};
const ART_NAMES = {json.dumps({f: t for f, _, t in LOTE1})};
const VIEWS = ['presentacion', 'estrategia', 'funnel', 'copys', 'landings'];

function loadFrame(id) {{
  const f = document.getElementById(id);
  if (f && !f.srcdoc && f.dataset.srcdoc) {{ f.srcdoc = f.dataset.srcdoc; }}
}}
function show(view, anchor) {{
  if (!VIEWS.includes(view)) view = 'presentacion';
  VIEWS.forEach(v => {{ document.getElementById('v-' + v).hidden = v !== view; }});
  document.querySelectorAll('.tab').forEach(t => {{ if (t.dataset.view === view) t.setAttribute('aria-current', 'page'); else t.removeAttribute('aria-current'); }});
  if (view === 'presentacion') loadFrame('f-deck');
  if (view === 'funnel') loadFrame('f-funnel');
  if (anchor) {{ const el = document.getElementById(anchor); if (el) el.scrollIntoView(); }} else window.scrollTo(0, 0);
}}
function route() {{
  const h = decodeURIComponent(location.hash.slice(1));
  if (VIEWS.includes(h)) return show(h);
  // Anclas internas (índices de documentos)
  const el = h && document.getElementById(h);
  if (el) {{ const v = el.closest('.view'); show(v.id.slice(2), h); return; }}
  show('presentacion');
}}
window.addEventListener('hashchange', route);
route();

// Presentación
const deck = document.getElementById('f-deck');
const key = k => {{ try {{ deck.contentDocument.dispatchEvent(new KeyboardEvent('keydown', {{key: k}})); deck.contentWindow.focus(); }} catch (e) {{}} }};
document.getElementById('d-prev').onclick = () => key('ArrowLeft');
document.getElementById('d-next').onclick = () => key('ArrowRight');
document.getElementById('d-full').onclick = () => {{
  const r = deck.requestFullscreen ? deck.requestFullscreen() : null;
  if (r && r.catch) r.catch(() => {{ document.getElementById('d-full').textContent = 'Pantalla completa no disponible aquí'; }});
  setTimeout(() => {{ try {{ deck.contentWindow.focus(); }} catch (e) {{}} }}, 300);
}};
deck.addEventListener('load', () => {{ try {{ deck.contentWindow.focus(); }} catch (e) {{}} }});

// Funnel: el enlace a la landing abre la pestaña de landings
document.getElementById('f-funnel').addEventListener('load', e => {{
  try {{ e.target.contentDocument.addEventListener('click', ev => {{ const a = ev.target.closest('a[href="#landings"]'); if (a) {{ ev.preventDefault(); location.hash = 'landings'; }} }}); }} catch (err) {{}}
}});

// Visor de artes
const lb = document.getElementById('lb');
document.addEventListener('click', e => {{
  const b = e.target.closest('[data-lb]'); if (!b) return;
  lb.querySelector('img').src = window.SUITE_PIECES[b.dataset.lb]; lb.querySelector('img').alt = ART_NAMES[b.dataset.lb] || '';
  lb.querySelector('p').textContent = (ART_NAMES[b.dataset.lb] || '') + ' · ' + b.dataset.lb; lb.hidden = false; lb.querySelector('.x').focus();
}});
lb.addEventListener('click', e => {{ if (e.target.tagName !== 'IMG') lb.hidden = true; }});
document.addEventListener('keydown', e => {{ if (e.key === 'Escape') lb.hidden = true; }});

// Landings
function land(k) {{
  const d = LANDS[k]; if (!d) return;
  document.querySelectorAll('.seg').forEach(s => s.setAttribute('aria-pressed', s.dataset.land === k));
  document.getElementById('l-desk').src = d.desk; document.getElementById('l-desk').alt = d.name + ' · ' + d.state + ' · escritorio';
  document.getElementById('l-mob').src = d.mob; document.getElementById('l-mob').alt = d.name + ' · ' + d.state + ' · móvil';
  document.getElementById('l-url').textContent = d.url;
  document.getElementById('l-name').textContent = d.name;
  const st = document.getElementById('l-state'); st.textContent = d.state; st.classList.toggle('pre', d.state === 'Preventa');
  document.getElementById('l-note').textContent = d.note;
  document.querySelectorAll('.screen').forEach(s => s.scrollTop = 0);
  try {{ localStorage.setItem('suite-land', k); }} catch (e) {{}}
}}
document.querySelectorAll('.seg').forEach(s => s.addEventListener('click', () => land(s.dataset.land)));
let savedLand = 'reloj'; try {{ savedLand = localStorage.getItem('suite-land') || 'reloj'; }} catch (e) {{}}
land(LANDS[savedLand] ? savedLand : 'reloj');
</script>
"""

out = pathlib.Path(sys.argv[1]); out.write_text(page, encoding='utf-8')
print(out, f'{out.stat().st_size/1e6:.1f} MB')
