# Lanzamiento Q4 2026: Gestión de Personal, Reclutamiento y Reloj Checador

Material de Marketing/Growth para el lanzamiento acordado en la sesión *Product Launch | GP, Rec, Reloj* (3-nov-2026).

| Archivo | Qué es |
|---|---|
| [`estrategia.md`](estrategia.md) | Estrategia integral: objetivos, posicionamiento, fases, canales, calendario, presupuesto, KPIs, riesgos y responsables |
| [`copys.md`](copys.md) | Copys listos para usar: ads, posts, emails, WhatsApp, in-app, guion de webinar y briefs de artes |
| [`reloj-checador.html`](reloj-checador.html) | Landing de Reloj Checador (preventa / lista prioritaria + registro al webinar) |
| [`gestion-personal.html`](gestion-personal.html) | Landing de Gestión de Personal (disponible, agenda demo) |
| [`reclutamiento.html`](reclutamiento.html) | Landing de Reclutamiento (disponible, agenda demo) |
| [`index.html`](index.html) | **Visor**: navega todos los archivos (deck, estrategia, copys y landings con vista móvil) |
| [`artes/claude-design.md`](artes/claude-design.md) | **Artes**: prompt para Claude Design, piezas por lote (webinar para el 13-nov) y recursos en `artes/recursos/` (capturas del widget, logos, Lapzi, fuentes, Figma) |
| [`funnel.html`](funnel.html) | **Funnel** estilo Funnelytics: fuentes → captura → webinar → preventa → ventas, en dos carriles (clientes / no clientes), con metas proyectadas, presupuesto, dueños y accionables por semana |
| [`funnel-standalone.html`](funnel-standalone.html) | El mismo funnel en **un solo archivo** (fuentes y artes incrustados) para abrirlo en local con doble clic. Se regenera con `python3 lanzamiento/scripts/build-funnel-standalone.py` cuando agregues artes a `artes/piezas/` |
| [`deck.html`](deck.html) | Deck para presentar la estrategia al equipo (flechas ← → para navegar) |

`reloj-checador.html` está construida con el design system de `Lapzo-Growth/lapzo-marketing-studio` (tokens `--lz-*`, Degular/Poppins y patrones de las landings `/lp/`); sus fuentes, íconos, Lapzi y logos están en `lz/`. El widget de Control Horario (`lz/control-horario.js`) reproduce los 6 estados del Figma *Control Horario · Componentes — Opción A*. Las otras dos landings usan `../design-system/` (tokens, fuentes, logos, Lapzi). Los formularios están marcados con `<!-- HUBSPOT -->`: hay que reemplazarlos por el embed del form de HubSpot correspondiente antes de publicar.
