# Artes del lanzamiento con Claude Design

Todo lo necesario para producir los artes de la campaña en Claude Design: el prompt maestro, las piezas por lote con sus textos finales y los recursos que hay que adjuntar.

**Lote 1 (webinar) se necesita el viernes 13-nov** para subir la pauta a revisión y que corra desde el lunes 16-nov.

---

## 1. Cómo usarlo

1. Abre un proyecto nuevo en Claude Design. Si ya existe el design system de Lapzo (el de *Landings Campañas v2*), selecciónalo.
2. Adjunta los recursos de `artes/recursos/` (o el `.zip`). Como mínimo: `marca/lapzo-logo-blanco.svg`, `marca/lapzo-logo-color.png`, todo `producto/`, `lapzi/lapzi-pointing-right.png` y `lapzi/lapzi-thinking.png`. Si deja subir fuentes, sube también `fuentes/`.
3. Pega el **prompt maestro** (§2) como primer mensaje.
4. Pide cada lote con su bloque de §3. Revisa con el checklist de §5 antes de exportar.
5. Exporta en PNG a 1x (los tamaños ya son los de las plataformas) y nombra los archivos como dice la columna *Archivo*.

---

## 2. Prompt maestro

```
Eres el diseñador de la campaña de lanzamiento de Lapzo, una plataforma de talento para empresas en México y LATAM. Vas a crear artes para anuncios de LinkedIn y Meta, headers de email y banners. Todas las piezas son de la misma campaña y deben verse como un sistema.

CONTEXTO
- Campaña paraguas: "Tu gente, de principio a fin". Lapzo lanza 3 productos: Reclutamiento y Gestión de Personal (ya disponibles) y Reloj Checador (llega el 31 de diciembre de 2026).
- Gancho principal: la reforma laboral en México obliga a llevar un registro electrónico de la jornada desde el 1 de enero de 2027.
- Evento: webinar gratuito "Registro electrónico de jornada 2027: lo que tu empresa debe tener listo el 1 de enero". Martes 24 de noviembre, 10:00 (CDMX), en línea. Con Pedro Sors (Lapzo) y un especialista laboral invitado.
- Audiencia: directores y equipos de RH, y dirección general, de empresas medianas y grandes en México.

DESIGN SYSTEM (el de las landings de lapzo.co)
- Fondo principal oscuro "ink" #211435, con 1 o 2 manchas de luz difuminadas: violeta #7D4DE5 (opacidad 35%, blur muy alto) y magenta #CD519D (22%). Alternativa clara: fondo #F7F8F9 con tarjetas blancas.
- Acento de texto sobre oscuro: lila #C7A4FF (para la parte destacada del titular). Botón principal: #7D4DE5 con texto blanco, radio 12px.
- Colores de producto (detalles, nunca fondos completos): violeta #A996FF (tiempo trabajado), aqua #A4E4E5 (descansos), naranja #FEC195 (horas extra).
- Titulares: LZ Degular Bold (si no está disponible, una grotesca geométrica condensada y pesada), interlineado apretado (1.0–1.05), tracking -2%, en oración (no todo en mayúsculas). Una parte del titular va en lila #C7A4FF.
- Texto: Poppins Regular/Medium. Etiquetas pequeñas: Poppins SemiBold 12–14 px, MAYÚSCULAS, tracking +8%, en lila.
- "Eyebrow"/chip: rectángulo con radio 4px, fondo lila al 14% y texto lila, con un ícono de destello.
- Logo: lapzo-logo-blanco.svg sobre oscuro, lapzo-logo-color.png sobre claro. Siempre en una esquina superior, pequeño.
- Mascota: Lapzi (archivos lapzi-*.png). Úsala como acento con un halo violeta difuminado detrás, nunca más grande que el mockup de producto.
- Producto: usa SOLO las capturas reales adjuntas (widget-*.png, app-mi-perfil-*.png, boton-topnav-*.png, notificacion-*.png). Colócalas en tarjetas con radio 16–24px y sombra profunda (0 30px 80px rgba(0,0,0,.45)). Puedes inclinarlas ligeramente o superponer una notificación sobre el widget. No redibujes ni inventes pantallas.

TONO Y REGLAS DE CONTENIDO
- Español de México, claro y directo. Lapzo es un "aliado", no una "plataforma". Decimos "colaboradores", no "empleados".
- No prometer lo que no existe: nada de nómina, huella/biométricos, reconocimiento facial, geolocalización, modo kiosco ni firma digital. Nunca decir "cumple al 100% con la ley". Reloj Checador siempre "llega el 31 de diciembre", nunca "ya disponible" (hasta el 5 de enero).
- Usa exactamente los textos que te doy para cada pieza. No agregues cifras, precios ni testimonios.

COMPOSICIÓN
- Una idea por pieza: titular grande + 1 apoyo + chip de fecha + CTA (si aplica) + mockup de producto.
- Texto mínimo en anuncios: el titular debe leerse en 1 segundo en un teléfono.
- Márgenes de 64px en 1080 px de ancho; en stories deja libres 250px arriba y abajo.
- Contraste AA en todo el texto.

Confirma que entendiste el sistema y espera el primer lote.
```

---

## 3. Piezas por lote

### Lote 1: webinar (para el viernes 13-nov)

Pégalo así:

```
LOTE 1: webinar del martes 24 de noviembre. Crea estas 6 piezas con el sistema que te di. Todas llevan el chip "Webinar gratuito · Mar 24 nov · 10:00 CDMX".
```

…y luego la tabla:

| # | Archivo | Formato | Titular (lila entre *asteriscos*) | Apoyo | CTA en el arte | Visual |
|---|---|---|---|---|---|---|
| 1 | `li-webinar-ley-1200x627.png` | 1200×627 (LinkedIn) | El 1 de enero el registro de jornada *deja de ser opcional.* | Lo que tu empresa debe tener listo, en 45 minutos. | Regístrate gratis | `widget-4-confirmar-cierre.png` a la derecha, con `notificacion-jornada-finalizada.png` encima |
| 2 | `li-webinar-horas-extra-1200x627.png` | 1200×627 (LinkedIn) | Las horas extra que no registras *son un riesgo.* | Aprende a preparar jornadas, turnos y horas extra para 2027. | Regístrate gratis | `widget-6-horas-extra.png` (resalta el tramo naranja después de las 18:00) |
| 3 | `li-webinar-ley-1080x1080.png` | 1080×1080 (LinkedIn) | El 1 de enero el registro de jornada *deja de ser opcional.* | Webinar con Pedro Sors y un especialista laboral. | Regístrate gratis | `app-mi-perfil-4-confirmar-cierre.png` recortada, saliendo por la esquina inferior derecha |
| 4 | `meta-webinar-excel-1080x1080.png` | 1080×1080 (Meta feed) | ¿Todavía registras asistencias *en Excel?* | El 1 de enero cambia la regla. | Aparta tu lugar | `widget-2-trabajando.png` + `lapzi-thinking.png` pequeño a un lado |
| 5 | `meta-webinar-agenda-1080x1350.png` | 1080×1350 (Meta feed vertical) | Lo que tu empresa debe tener listo *el 1 de enero* | Lista: 1) La reforma en 10 minutos. 2) Las 5 claves para jornadas, turnos y horas extra. 3) Demo de Reloj Checador. 4) Preguntas en vivo. | Aparta tu lugar | `widget-1-sin-iniciar.png` abajo, con `boton-topnav-1-sin-iniciar.png` |
| 6 | `meta-webinar-story-1080x1920.png` | 1080×1920 (Stories/Reels) | El registro de jornada *ya tiene fecha.* | 1 de enero de 2027. Prepárate con nosotros el martes 24 de noviembre. | Desliza para registrarte | `widget-4-confirmar-cierre.png` grande al centro + `lapzi-pointing-right.png`; respeta 250px libres arriba y abajo |

Textos que acompañan cada anuncio en la plataforma: `copys.md` §11 (L1 y L2 para las piezas 1–3; M1 para 4–6).

### Lote 2: lanzamiento de la suite (para el lunes 16-nov)

```
LOTE 2: anuncio de la suite "Tu gente, de principio a fin". Tres tarjetas escalonadas, una por producto, cada una con su etiqueta: Reclutamiento (Disponible), Gestión de Personal (Disponible), Reloj Checador (Llega el 31 de diciembre). Fondo ink con manchas violeta y magenta. Lapzi: lapzi-yougotthis.png.
```

| # | Archivo | Formato | Titular | Apoyo |
|---|---|---|---|---|
| 7 | `suite-1200x627.png` | 1200×627 | Tu gente, *de principio a fin.* | Atrae, administra y registra la jornada de tu gente con el mismo aliado. |
| 8 | `suite-1080x1080.png` | 1080×1080 | Tu gente, *de principio a fin.* | Reclutamiento · Gestión de Personal · Reloj Checador |
| 9 | `suite-1080x1350.png` | 1080×1350 | Tu gente, *de principio a fin.* | Reclutamiento · Gestión de Personal · Reloj Checador |
| 10 | `email-header-suite-600x200.png` | 600×200 (exporta a 1200×400) | Tu gente, *de principio a fin.* | — |
| 11 | `email-header-webinar-600x200.png` | 600×200 (exporta a 1200×400) | Registro de jornada 2027 | Webinar · Mar 24 nov · 10:00 CDMX |
| 12 | `email-header-reloj-600x200.png` | 600×200 (exporta a 1200×400) | Reloj Checador *llega el 31 de diciembre.* | — |
| 13 | `inapp-banner.png` | Confirmar medida con Producto (propuesta 1200×200) | *Nuevo en Lapzo:* Gestión de Personal y Reclutamiento ya están aquí. | Reloj Checador llega el 31-dic · Botón "Regístrate al webinar del 24-nov" |

### Lote 3: después del webinar (para el 25-nov en adelante)

| # | Archivo | Formato | Titular | Notas |
|---|---|---|---|---|
| 14 | `preventa-1080x1080.png` y `-1200x627.png` | 1080×1080, 1200×627 | Asegura tu lugar en la *primera ola* de enero. | `widget-5-jornada-finalizada.png`. CTA "Únete a la lista prioritaria" |
| 15 | `countdown-30d.png`, `-14d.png`, `-7d.png` | 1080×1080 | Faltan *30 / 14 / 7 días* para el registro electrónico de jornada. | Publicar 2-dic, 18-dic y 25-dic (orgánico). Número gigante en lila |
| 16 | `carrusel-que-cambia-1..6.png` | 1080×1350 × 6 | Ver `copys.md` §9 (carrusel "Qué cambia el 1 de enero") | Slide 1 portada, 2–5 un dato por slide, 6 CTA |
| 17 | `ya-esta-aqui-*.png` | 1080×1080, 1200×627, 1080×1920 | Reloj Checador *ya está aquí.* | **No publicar antes del 5-ene.** Cambia el chip a "Disponible" |

---

## 4. Recursos (`artes/recursos/`)

| Carpeta | Qué hay | Para qué |
|---|---|---|
| `producto/` | Capturas del widget de Control Horario a 3x con fondo transparente: 6 estados (`widget-1` … `widget-6`), el botón del topnav en cada estado, 4 notificaciones y la pantalla *Mi Perfil* completa en 2 estados | Mockups de producto. Son reproducción fiel del Figma *Control Horario · Opción A* |
| `figma/` | Exportes originales del Figma (topnav web 1440 y 5 estados) | Referencia; no usar en piezas si ya hay versión en `producto/` |
| `marca/` | Logo blanco (SVG), logo a color y sobre oscuro (PNG), símbolo | Logo de cada pieza |
| `lapzi/` | Lapzi señalando, pensando, celebrando, "you got this", escribiendo y con destello | Acento de personaje |
| `fuentes/` | LZ Degular Bold/Semibold, Poppins Regular/Medium/SemiBold | Subir a Claude Design si lo permite |

**Tokens de color** (de `lapzo-marketing-studio/components/lp-mkt/lp-mkt.css`):

| Token | Hex | Uso |
|---|---|---|
| `--lz-marketing-ink` | `#211435` | Fondo principal |
| `--lz-marketing-action` | `#7D4DE5` | Botón, manchas de luz |
| `--lz-marketing-highlight` | `#C7A4FF` | Parte destacada del titular, etiquetas |
| `--lz-brand-30` | `#A996FF` | Tiempo trabajado en el widget |
| `--lz-aqua-30` | `#A4E4E5` | Descansos |
| `--lz-orange-30` | `#FEC195` | Horas extra |
| `--lz-magenta-60` | `#CD519D` | Segunda mancha de luz |
| `--lz-neutral-80` | `#14142A` | Fondo del widget |
| `--lz-neutral-20` | `#F7F8F9` | Fondo claro |

---

## 5. Checklist antes de exportar

- [ ] El texto es exactamente el de la tabla (sin cifras, precios ni testimonios añadidos).
- [ ] Fecha y hora correctas: **martes 24 de noviembre, 10:00 CDMX**.
- [ ] Reloj Checador aparece como "llega el 31 de diciembre" (salvo el lote "ya está aquí").
- [ ] El producto es una captura real de `producto/`, sin pantallas inventadas.
- [ ] Nada de nómina, biométricos, geolocalización, kiosco, firma digital ni "cumple al 100%".
- [ ] El titular se lee en un teléfono; contraste suficiente.
- [ ] Stories: 250px libres arriba y abajo.
- [ ] Logo presente y legible.
- [ ] Nombre de archivo según la tabla.
