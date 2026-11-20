# Handoff: lanzamiento Q4 Lapzo y webinar de Reloj Checador (1-dic-2026)

Contexto para continuar este trabajo en otra sesión de Claude Code. Actualizado: 20-nov-2026.

> ⚠️ Este repositorio se puede leer públicamente. Este archivo no contiene contraseñas, tokens, correos personales ni el link de Zoom. Esos datos están en HubSpot y Zoom.

## 1. Qué es el proyecto

Es el lanzamiento Q4 de tres productos de Lapzo: Gestión de Personal, Reclutamiento y Reloj Checador. Lo lleva Diego (Marketing).

La pieza activa ahora es el **webinar gratuito "Registro electrónico de jornada 2027: lo que tu empresa debe tener listo el 1 de enero"**:
- Fecha: **martes 1 de diciembre de 2026, 10:00 a 11:00 (CDMX)**, por Zoom.
- Captación: del 16 al 30 de noviembre, con Meta Ads hacia una landing en lapzo.com.
- Panel:
  - Pedro Sors (COO, modera)
  - Carolina Archila (Producto)
  - Especialista laboral (por confirmar)
  - Líder de RH de un cliente (por confirmar)

Reglas de trabajo con Diego:
- Escribir en español, con tono corporativo. Usar solo nombres de pila.
- Confirmar antes de publicar, activar gasto, mandar correos o integrar a producción.
- No crear PRs si no lo pide.

## 2. Repositorios

| Repo | Para qué | Rama de trabajo |
|---|---|---|
| `diegocuauhtemoc-lapzo/MarketingGrowth` (este) | Estrategia, copys, deck, funnel, artes, la landing anterior de HubSpot y el contenedor de GTM | `claude/nice-wozniak-lbf801` (PR #1 contra `main`) |
| `Lapzo-Growth/lapzo-marketing-studio` | Sitio www.lapzo.com (Next.js "vinext"; Railway lo despliega desde `main`, detrás de CloudFront) | `claude/lp-webinar-reloj-1dic` (PR #36) |

Archivos clave en **MarketingGrowth**:
- Estrategia y plan:
  - `lanzamiento/estrategia.md`
  - `lanzamiento/copys.md`
  - `lanzamiento/deck.html`
  - `lanzamiento/funnel.html`
  - `lanzamiento/lanzamiento-q4.html`: página única con todo. También está publicada como artifact: https://claude.ai/artifact/VrfUjqFLU4U7UV5SU8CnMG
- Artes oficiales del webinar del 1-dic: `lanzamiento/artes/piezas/` (meta-webinar-excel, meta-webinar-agenda, meta-webinar-story y las piezas li-*).
- Contenedor importable de GTM: `lanzamiento/gtm/gtm-webinar-reloj-1dic.json`.
- Landing anterior de HubSpot, en HubL: `lanzamiento/hubspot/webinar-registro-jornada-2027.hubl.html`. Se genera con `lanzamiento/scripts/build-hubspot-webinar.py`.

Archivos clave en **lapzo-marketing-studio** (PR #36):
- `app/lp/webinar-registro-jornada-2027/page.tsx`: metadata con noindex,follow.
- `components/lp-webinar/webinar-landing.tsx`: la landing, el formulario de HubSpot, el dataLayer y el Lead de Meta.
- `components/lp-webinar/webinar.css`
- `public/lp-mkt/assets/webinar/pedro-sors.jpg`
- `scripts/check-layout.mjs`: tiene las secciones `lzw-*` agregadas.

Reglas del repo del sitio (AGENTS.md):
- Usar `ds-section` dentro de `.lapzo-home`, sin gutters propios.
- `npm ci` y luego `npm run build`; el build corre `check:layout`.
- Las landings van bajo `/lp/*` con noindex.

## 3. Conectores que necesita la otra cuenta

1. **GitHub**, con acceso de escritura a los dos repos. En Claude Code en la web hay que agregarlos como fuentes, o usar `add_repo`.
2. **Facebook Ads (Meta)**, con acceso a la cuenta publicitaria "Lernit - Lapzo".
3. **HubSpot**, en el portal de Lapzo (19559790).
4. Opcionales:
   - **Gmail**: para avisos al equipo.
   - **Google Calendar**.

## 4. IDs y estado actual

### HubSpot (portal 19559790)
- Formulario **"[MKT] Formulario Webinar"**, GUID `9395ea23-312f-44c3-93ff-188c04cfe1e2`.
  - Link para compartir: https://share.hsforms.com/1k5XqIzEvRMOT_xiMBM_h4gbn8f. Hoy da error; hay que revisar en el formulario → Compartir. No es crítico.
- Workflow simple "Enviar correo luego del envío de formularios", creado desde la pestaña Automatización del formulario: **ACTIVADO**.
  - Envía el correo **"[MKT] Confirmación Webinar 1-dic"**, que ya tiene el link de Zoom y el de "Agregar a mi calendario".
  - La reinscripción está activada.
- Landing anterior en HubSpot: contentId `227885236564`, plantilla `custom/content-mcp/pages/webinar-registro-jornada-2027.html` (templateId `227885465648`).
  - Está **publicada** en https://recursos.lapzo.com/webinar-registro-jornada-2027.
  - Falta decidir si se despublica o se redirige cuando la de lapzo.com esté en línea.

### Meta Ads (cuenta `715031048874224` "Lernit - Lapzo", MXN)
- Página Lapzo `600213766833074`, IG go_lapzo `17841467594803052`, **Lernit Pixel `337850720804196`**.
- Campaña `120251032624630207` "RC_Webinar1dic_Leads_MX_CBO_Nov26":
  - OUTCOME_LEADS con CBO.
  - Presupuesto total de $4,000 MXN.
  - **En borrador, sin publicar.**
- Conjunto de anuncios `120251032627120207` "RC_Webinar1dic_MX_RH_Broad_A+A":
  - Optimiza a OFFSITE_CONVERSIONS con el evento LEAD del pixel.
  - México, 28 a 55 años, Advantage+ audience.
  - Termina el 2026-11-30 a las 23:59 (CDMX).
- Anuncios en borrador:
  - `120251032666440207` "RC_Webinar1dic_Excel", creativo `1776663950295916`.
  - `120251032668080207` "RC_Webinar1dic_Agenda", creativo `943203332058100`.
  - Hoy apuntan a **recursos.lapzo.com** (la landing de HubSpot). **Hay que cambiarlos.**
- Hashes de imagen:
  - Excel: `d4881d4c8af8a960566dd50339e19ce9`
  - Agenda: `db28cc00505cb85c2a87813835afbc4a`
  - Story 9:16: `d3339a62de8a5224b910139afa3e5c7f`
- Creativos:
  - PAC: feed con la imagen 1:1 o 4:5 y story/reels con la 9:16.
  - CTA: SIGN_UP.
- url_tags: `utm_source=meta&utm_medium=paid_social&utm_campaign=suite-lanzamiento-q4&utm_term=webinar-1dic&utm_content=meta-webinar-excel` (o `meta-webinar-agenda`).
- Para publicar la campaña se usa `ads_activate_entity` sobre la campaña. Solo cuando Diego lo confirme.

### Medición
- GTM **GTM-KPTJ5JG**: es el contenedor de lapzo.com y ya se carga en todo el sitio (`app/layout.tsx`).
- Eventos de dataLayer en la landing nueva:
  - `webinar_landing_view`: lleva webinar_id, ad_platform y ad_campaign.
  - `webinar_registro`: se dispara solo cuando HubSpot confirma el envío, una vez por visita. Lleva event_id, webinar_id `reloj-webinar-1dic`, form_id, lead_type, lead_landing, ad_platform y ad_campaign.
- El **Lead de Meta** se dispara desde la página, con `eventID` igual a `event_id`. **En GTM no debe existir otra etiqueta de Lead de Meta para este evento.**
- Pendiente de Diego en GTM:
  1. Importar `lanzamiento/gtm/gtm-webinar-reloj-1dic.json`.
  2. Cambiar `G-XXXXXXXXXX` por el ID de GA4.
  3. Revisar si ya hay etiquetas genéricas de formulario de HubSpot hacia Meta Lead, porque duplicarían los leads.
  4. Probar en Preview y publicar.
- El pixel también recibe Lead de otros sitios. Se recomienda crear una conversión personalizada: Lead filtrado por URL que contenga `webinar-registro-jornada-2027`.

## 5. Pendientes, en orden

1. [ ] **Integrar el PR #36** de `Lapzo-Growth/lapzo-marketing-studio`.
   - Está bloqueado por protección de rama: requiere la aprobación de una persona. El check `validate` ya pasó.
   - Diego lo aprueba y lo integra, o le pide a alguien del equipo que lo haga.
   - Railway lo publica en https://www.lapzo.com/lp/webinar-registro-jornada-2027.
2. [ ] Verificar que la URL nueva carga y que el formulario aparece.
3. [ ] **Cambiar los anuncios de Meta a la URL nueva.**
   - El link de un creativo existente no se puede editar. Hay que crear dos creativos nuevos con los mismos hashes, copys, CTA y url_tags, con link `https://www.lapzo.com/lp/webinar-registro-jornada-2027`.
   - Después, actualizar los dos anuncios en borrador para que usen los creativos nuevos.
4. [ ] **Prueba en GTM Preview** sobre la URL nueva, con un registro real (`correo+testN@lapzo.com`). Revisar:
   - que `webinar_registro` aparezca una sola vez;
   - que el Lead de Meta llegue con eventID (Meta Events Manager → Probar eventos);
   - que el correo de confirmación llegue.
5. [ ] **Activar la campaña de Meta**, solo con la confirmación explícita de Diego.
6. [ ] Decidir qué pasa con la landing de HubSpot en recursos.lapzo.com: despublicarla o redirigirla.
7. [ ] Pendientes menores:
   - Correos de recordatorio del 30-nov y del 1-dic.
   - Correo post-webinar con la grabación el 2-dic y preventa el 3-dic (ver `lanzamiento/estrategia.md`).
   - Confirmar los dos invitados del panel.
   - Decidir FitchUp o Fichap.

## 6. Ya hecho
- Estrategia, copys, deck, funnel, landings de producto y página única, con todas las fechas movidas al 1-dic.
- Campaña de Meta armada en borrador con los artes oficiales del 1-dic.
- Formulario de HubSpot, correo de confirmación con Zoom y workflow activo. Ya se probó un envío desde la landing de HubSpot y se mostró el mensaje de éxito.
- Landing en el sitio (PR #36): build y QA en Playwright en escritorio y móvil. Se probó que se registra un solo `webinar_registro` aunque lleguen dos envíos.
