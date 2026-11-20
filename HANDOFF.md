# Handoff — Landing TaaS (Lapzo)

Contexto para continuar este proyecto desde otra cuenta/sesión de Claude Code.

## Qué es esto

Landing page de **TaaS (Talent-as-a-Service)** para Lapzo, construida en HTML/CSS estático
con el design system real de la marca (no un framework, no build step).

- **Rama de trabajo:** `claude/happy-ramanujan-jycdxu`
- **Página:** `taas/index.html` — ábrela en el navegador o sírvela con
  `python3 -m http.server` desde la raíz del repo.
- **Design system:** `design-system/` — tokens (`colors_and_type.css`), fuentes
  (Poppins, Space Grotesk, Degular), logo, íconos, decor, mascota Lapzi, íconos de
  módulo y logos de clientes. Reutilizable para futuras landings.
- **Manual de marca completo:** `design-system/brand-manual.md` — **leer antes de
  escribir o tocar cualquier copy o decisión de diseño.** Incluye buyer personas,
  reglas de voz/tono no negociables, paleta, tipografía y casos de éxito verificados.

## Reglas de marca no negociables (resumen — ver el manual para el detalle)

1. Lapzo es "aliado estratégico", nunca "plataforma" ni "software".
2. "Colaboradores", nunca "empleados".
3. Títulos en minúscula (solo la primera letra en mayúscula). Sin signos de exclamación.
4. Nunca `#000000` puro — texto en claro es `#3F3F46`, fondo oscuro es `#14142A`.
5. Botones siempre pill (`border-radius: 9999px`), violeta `#8B55FE`, Poppins SemiBold.
6. H1 en Space Grotesk/Degular; todo lo demás en Poppins.
7. Nunca inventar clientes, cifras o casos de éxito — solo usar los que están en
   `brand-manual.md` sección 14.
8. CTAs verbo-primero ("Agenda tu diagnóstico", nunca "Click aquí" o "Enviar").

## Buyer personas usadas en esta landing

TaaS está dirigido a empresas de **25–60 colaboradores**. Los dos personas que
guían el copy (ver `brand-manual.md` sección 12):

- **Sofía** — profesional de RH multi-rol (sola hace selección + capacitación +
  desempeño). Persona principal.
- **Santiago** — directivo/CEO, orientado a ROI y resultados de negocio. Decisor
  secundario.

## Estado actual

- [x] Design system importado al repo (`design-system/`)
- [x] Landing completa: hero, dolores, cómo funciona, módulos incluidos, 3 pilares
      de marca, tabs de persona (Sofía/Santiago), checklist "¿es TaaS para ti?", FAQ,
      CTA final, footer.
- [x] Validado visualmente en desktop y mobile (Playwright/Chromium).
- [ ] **Pendiente:** los CTAs "Agenda tu diagnóstico" y "Habla con un experto"
      apuntan a `#` — falta la URL real (Calendly, HubSpot form, WhatsApp, etc.)
- [ ] Pendiente: definir dónde se despliega en producción (HubSpot, Webflow,
      estático en Vercel/Netlify, etc.) — por ahora es HTML standalone en el repo.
- [ ] Pendiente: conectar analítica/tracking si aplica.

## Conectores / accesos usados en esta sesión

- **GitHub** — único conector necesario para seguir editando este repo
  (`diegocuauhtemoc-lapzo/MarketingGrowth`).
- El design system se recibió como un .zip subido al chat (no vía conector) y ya
  quedó commiteado en `design-system/` — no hace falta volver a subirlo.
- No se usó ningún otro conector (HubSpot/Webflow/etc.) para esta landing; si la
  siguiente sesión va a publicarla en una de esas plataformas, necesitará ese
  conector conectado en su cuenta.

## Cómo seguir

1. Clonar/abrir el repo en la rama `claude/happy-ramanujan-jycdxu`.
2. Leer este archivo y `design-system/brand-manual.md`.
3. Para previsualizar: `cd` a la raíz del repo y `python3 -m http.server 8000`,
   luego abrir `http://localhost:8000/taas/index.html`.
4. Resolver los pendientes de arriba, empezando por las URLs reales de los CTAs.
