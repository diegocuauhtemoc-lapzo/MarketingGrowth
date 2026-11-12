# Estrategia integral de lanzamiento: Gestión de Personal, Reclutamiento y Reloj Checador

**Responsable:** Diego Cuauhtémoc (Growth)
**Versión:** 1.0, borrador para la sesión de seguimiento (jueves 10:30)
**Fuente:** sesión *Product Launch | GP, Rec, Reloj* del 3-nov-2026 con Vivian Cazadero, Pedro Sors, Fernando Núñez, Carolina Archila y Diego Cuauhtémoc.

---

## 0. Resumen ejecutivo

- **Qué lanzamos.** Tres productos que convierten a Lapzo en suite: **Gestión de Personal (GP)** y **Reclutamiento**, que ya se pueden vender y habilitar, y **Reloj Checador**, que se vende desde ya, tiene su release final el **31-dic-2026** y se habilita a clientes la **2.ª semana de enero 2027**.
- **Por qué ahora.** La reforma a la LFT (jornada de 40 horas) obliga a las empresas a llevar un **registro electrónico de la jornada a partir del 1-ene-2027**. Las multas reportadas llegan a cerca de **$590 mil MXN**. Es el único de los tres productos con *momentum* externo, y la competencia (Buk, Kerana, Runa) ya lo está aprovechando. Además, dic-ene es temporada alta de compra en RH por cierre y estreno de presupuesto.
- **Cómo.** Una sola campaña paraguas, **"Tu gente, de principio a fin"**, que arranca con **pauta desde el lunes 16-nov** y el **anuncio de la suite el martes 17-nov**, con el mismo mensaje en dos frentes:
  - **Hacia adentro (clientes):** anunciamos GP y Reclutamiento como *disponibles* y Reloj Checador como *próximamente*, con lista prioritaria. Lo usamos como palanca de cross-sell y retención (TaaS).
  - **Hacia afuera (no clientes):** usamos la ley como gancho, con un **webinar el martes 24-nov** ("Registro electrónico de jornada 2027: lo que tu empresa debe tener listo el 1 de enero"). Así generamos audiencia y leads *antes* del lanzamiento, para que el 31-dic/5-ene no empecemos de cero.
- **Metas (Pipeline + Preventa).** Propuesta a validar con Fer y Vips:
  - **60 SQLs**: 35 nuevos + 25 cross-sell.
  - **12 preventas de Reloj Checador** firmadas antes del 15-ene.
  - **300 registros** al webinar.
- **Presupuesto de pauta:** **$28,000 MXN** (tope < $30k), enfocado en registros al webinar y retargeting. Lo demás va por canales propios: email HubSpot, WhatsApp, in-app y orgánico.

---

## 1. Contexto y acuerdos de la sesión del 3-nov

| Tema | Acuerdo / estado |
|---|---|
| Fecha de arranque de comunicación | **17-nov**, para clientes y no clientes. *Ajuste del 12-nov: la pauta arranca antes, el lunes 16-nov, y el webinar se adelanta al martes 24-nov* |
| Release Reloj Checador | **31-dic** (Carolina); habilitación en instancia ~2.ª semana de enero |
| Material de producto para marketing | Desde la próxima semana, links de prueba semanales y Figmas de Reloj (reloj, configuración de jornada, turnos). En ~2 semanas: jornada, turnos y operación funcionales. Lo siguiente es reportería |
| Reloj Checador vs GP | **Módulos separados** por ahora (feature flag). Se pueden vender juntos como **bundle GP + Reloj** o por separado |
| Comunidad / anuncios | **No** se integra a GP. Sigue como módulo aparte y se usa como **regalo / gancho de cierre** |
| HR Agent | No está. Posible algo a fines de noviembre: **no comunicar** |
| Pricing | Pendiente. Fer y Diego traen benchmark y propuesta de cómo cotizar (por producto y por bundle). **No publicar precios** |
| Partners | No comunicar a clientes de **FitchUp** ni de **Worky** (quitarlos de *toda* lista de envío). Fer y Santiago hablan con Lucas (FitchUp) y Jimena (Worky) en las próximas 1–2 semanas. Pedro amarra la renovación de Tata antes de que se entere |
| Workshop | Sí. Lo puede dar Pedro (u otro vocero) |
| Ciclo de venta (Fer) | ~45 días |

### Alcance comunicable (lo que SÍ y lo que NO se puede prometer)

**Reloj Checador (release 31-dic)**
- ✅ Configuración de jornadas laborales
- ✅ Creación y asignación de turnos
- ✅ Registro de entradas y salidas (reloj checador) dentro de Lapzo
- ✅ Registro de descansos, confirmación de cierre de jornada, horas fuera de turno marcadas aparte y notificaciones en cada paso (según el Figma *Control Horario · Opción A*; **validar con Carolina que entra en el release del 31-dic** antes de comunicarlo en pauta)
- ✅ Solicitudes de corrección de marcación (p. ej., "olvidé marcar mi salida") con cadena de aprobación configurable
- 🔜 Reportería (lo siguiente en el roadmap; comunicar como "próximamente", sin fecha)
- ❌ Integración con nómina o con cualquier otro sistema (cero en este trimestre)
- ❌ Dispositivos biométricos o datos biométricos externos
- ❌ Geolocalización
- ❌ Modo kiosco

**Gestión de Personal (disponible)**
- ✅ Organigrama
- ✅ Expediente digital (ficha del colaborador: área, líder, a quién reporta, datos básicos)
- ✅ Solicitudes con cadenas de aprobación: vacaciones, licencias, permisos de todo tipo y cambio de datos personales
- ✅ Documentos: envío y requerimiento de documentos, incluida la constancia laboral (con o sin salario)
- ⚠️ **No hay firma digital.** El colaborador descarga, firma y vuelve a subir el documento. No usar las palabras "firma digital/electrónica" en ningún copy
- ❌ Anuncios / avisos emergentes (siguen en Comunidad, que podemos regalar)

**Reclutamiento (disponible)**
- ✅ Vacantes construidas por competencias (incluye Desarrollo por Competencias para cargar matrices, sin costo extra)
- ✅ IAMatch (match de candidatos con IA)
- ✅ Acceso facilitado a diagnósticos (se despliega la semana del 9-nov: confirmar con Carolina antes de comunicarlo)
- Modelo: precio por tamaño de empresa con vacantes y postulantes ilimitados (pendiente de validar con Fer)

> **Regla de oro del lanzamiento:** si Carolina no lo ha confirmado como incluido en el release, no aparece en ningún copy. Cada pieza pasa por un *check* de alcance de Producto antes de publicarse.

---

## 2. Objetivos y KPIs

Las metas cuantitativas son **hipótesis a validar** el jueves con Fer (ventas nuevas) y Vips/Pedro (base de clientes). Se calcularon con el ciclo de venta de 45 días y el presupuesto de pauta < $30k.

### Objetivo 1: Pipeline (SQLs)
| KPI | Meta propuesta | Fecha | Dueño |
|---|---|---|---|
| SQLs nuevos (no clientes) atribuidos a la campaña | 35 | 15-ene | Diego / Fer |
| Oportunidades de cross-sell en clientes (GP, Rec, Reloj) | 25 | 15-ene | Vips / Pedro |
| Valor de pipeline generado | Definir con el pricing de Fer | 15-ene | Fer |
| Tiempo de contacto a lead del webinar o landing | < 24 h hábiles | Continuo | Fer |

### Objetivo 2: Preventa Reloj Checador
| KPI | Meta propuesta | Fecha | Dueño |
|---|---|---|---|
| Inscritos a la *lista prioritaria* de Reloj | 150 empresas | 31-dic | Diego |
| Demos de Reloj (con prototipo/Figma) | 40 | 31-dic | Fer / Vips |
| Preventas de Reloj firmadas (solas o bundle GP + Reloj) | 12 | 15-ene | Fer / Vips |

### KPIs de soporte (salud del funnel)
| Métrica | Meta |
|---|---|
| Registros al webinar del 24-nov | 300 (≈60% externos, 40% clientes) |
| Asistencia en vivo | ≥ 35% de los registros |
| CPL de pauta (registro a webinar / lista) | ≤ $120 MXN |
| CTR de email a clientes | ≥ 3.5% |
| Conversión de landing a lead | ≥ 12% |
| MQL a SQL | ≥ 25% |

**Tracking:** UTMs por canal y pieza (`utm_campaign=suite-lanzamiento-q4`, `utm_content=<pieza>`). Cada producto usa un form de HubSpot propio, con la propiedad `producto_interes` (GP / Reclutamiento / Reloj / Bundle) y `es_cliente` (sí/no). El pixel de Meta y el Insight Tag de LinkedIn van en las 3 landings desde el día 1 para construir audiencias de retargeting.

---

## 3. Posicionamiento y mensajes

### Idea paraguas
> **"Tu gente, de principio a fin."**
> Lapzo ya desarrollaba a tu talento. Ahora también lo **atrae** (Reclutamiento), lo **administra** (Gestión de Personal) y **registra su jornada** (Reloj Checador), en el mismo lugar y con el mismo aliado.

Encaja con el posicionamiento de marca ("aliado estratégico", no "plataforma"). Responde además al *pain point* principal de Sofía y Pedro: demasiadas herramientas, fees y datos desconectados.

### Mensaje por producto
| Producto | Estado | Mensaje principal | Prueba / razón para creer | CTA |
|---|---|---|---|---|
| **Reloj Checador** | Próximamente (31-dic) | *"El 1 de enero el registro electrónico de jornada deja de ser opcional. Llega preparado."* | Jornadas, turnos, marcación y correcciones con aprobación, conectados al expediente de tu gente en Lapzo | Únete a la lista prioritaria / Regístrate al webinar |
| **Gestión de Personal** | Disponible | *"Solicitudes, documentos y expediente de tu gente sin perseguir a nadie por WhatsApp."* | Organigrama, expediente, solicitudes con cadenas de aprobación, constancias laborales | Agenda una demo |
| **Reclutamiento** | Disponible | *"Contrata por competencias, no por corazonadas."* | Vacantes por competencias + IAMatch, vacantes y postulantes ilimitados | Agenda una demo |
| **Bundle GP + Reloj** | Preventa | *"Tu gente y su jornada, en un solo lugar."* | Las solicitudes de vacaciones y de corrección de marcación viven juntas | Cotiza el bundle |

### Mensaje por ICP (Reloj Checador como gancho)
| ICP | Ángulo | Canal principal |
|---|---|---|
| **Pedro**, Director de RH (Tier 1-2) | Cumplimiento sin fricción + riesgo de multa + "no es otra herramienta, es tu mismo aliado" | LinkedIn, email, webinar |
| **Sofía**, RH multi-rol (Tier 3) | "Deja de cuadrar asistencias en Excel": centraliza jornada, solicitudes y documentos | Meta (IG), LinkedIn, WhatsApp |
| **Santiago**, Directivo (Tier 3) | Riesgo legal y control de horas extra: "cada minuto extra se paga" | LinkedIn, Google Search |
| **Andrea**, C&D (Tier 1-2), solo clientes | "Tu plataforma de capacitación ahora cubre la operación de tu gente": cross-sell | Email, in-app |

> Ojo con los nombres: "Pedro" y "Santiago" en esta tabla son los ICPs ficticios, no Pedro Sors ni Santiago Maldonado.

### Diferenciación frente a la competencia (uso interno, nunca nombrar competidores en piezas)
| Competidor | Qué está haciendo | Cómo respondemos |
|---|---|---|
| **Buk** | WhatsApp masivo de Reloj con urgencia; suite con nómina | No competimos en nómina. Competimos en *talento + operación* en un solo lugar y en acompañamiento (aliado, CS) |
| **Kerana** | Workshops presenciales de Reloj | Webinar del 24-nov + sesión presencial opcional para cuentas clave en enero (fase 2, si hay tracción) |
| **Runa** | ~$22 MXN por empleado con reloj | Insumo para el pricing de Fer y Diego. Comunicar bundle, no precio |
| **FitchUp / Worky** | Partners con clientes compartidos | Excluirlos de la comunicación. Mensajes que no los ataquen. Fer y Santiago llevan la conversación |

**Guardrails de copy.**
- No decir "cumple al 100% con la ley" ni "certificado por la STPS". Decir *"te ayuda a llevar el registro electrónico de jornada que pide la reforma"* (validar redacción con legal).
- No mencionar nómina, biométricos, geolocalización, kiosco ni firma digital.
- No publicar precios.
- Nunca decir "lo tenemos hoy" de Reloj: siempre *"llega el 31 de diciembre"* o *"próximamente"*.

---

## 4. Audiencias

### Hacia adentro: clientes actuales
| Segmento | Criterio (HubSpot) | Producto foco | Canal |
|---|---|---|---|
| A. Cuentas clave (Tier 1) | Top cuentas por ARR, con CSM asignado | Bundle GP + Reloj, Reclutamiento | Contacto 1:1 de CSM/Pedro + invitación personal al webinar |
| B. Clientes con plan multi-módulo | ≥ 2 módulos activos | GP + Reloj | Email + in-app + WhatsApp CSM |
| C. Clientes de 1 módulo (CyA) | 1 módulo activo | GP (retención) + Reloj | Email + in-app |
| D. Cuentas en riesgo / renovación ≤ 90 días | Lista de Vips | GP + Reloj como palanca de retención (TaaS) | 1:1 CSM |
| **EXCLUSIÓN** | Clientes que llegaron por o trabajan con **FitchUp** o **Worky** (incluye Tata) | — | **Ninguno**. Lista de supresión global en HubSpot, Meta (custom audience excluida) y WhatsApp |

> **Acción para el 13-nov:** Vips y Pedro entregan la lista de exclusión FitchUp/Worky. Diego crea la lista de supresión en HubSpot (`EXCL - Partners FitchUp Worky`) y la aplica a *todos* los envíos y audiencias.

### Hacia afuera: no clientes
- **Base propia:** leads y MQLs no convertidos de HubSpot en los últimos 18 meses, sin clientes ni exclusiones.
- **Pauta:** México, empresas de 50 a 5,000 colaboradores, en industrias con turnos (manufactura, retail, logística, farmacéutico, hotelería, automotriz). Cargos: Director/Gerente de RH, Jefe de Personal, Administración de Personal, Nóminas, Director General, Operaciones.
- **Retargeting:** visitantes de las 3 landings, registrados al webinar y engagement con videos o posts de Reloj.

---

## 5. Plan por fases

```
         NOV                         DIC                              ENE
 11  16 17 ──── 23 24 25 ───────── 15 ─── 24 ── 31      5 ─ 12 ──── 31
 [F0 Prep][F1+F2 Captación][F3 Webinar + Preventa ────────][F4 GA][ F5 Habilitación ]
          16-nov: arranca pauta    24-nov: webinar              31-dic release
          17-nov: anuncio suite                                 5-ene anuncio "ya está"
```

### F0: Preparación (11 al 15-nov)
| Entregable | Dueño | Fecha |
|---|---|---|
| Estrategia + copys + landings (este paquete) | Diego | 12-nov (sesión jueves) |
| Aprobación de alcance de copys por Producto | Carolina | 13-nov |
| Lista de exclusión FitchUp/Worky | Vips / Pedro | 13-nov |
| Forms HubSpot, UTMs, pixel Meta, Insight Tag LinkedIn y listas de segmentos | Diego | 13-nov |
| Artes de pauta (6 piezas del webinar) | Diseño (brief en `copys.md`) | **13-nov** (para subir campañas a aprobación ese día) |
| Artes restantes: key visual, banner in-app, header de email | Diseño | 16-nov |
| Campañas de LinkedIn, Meta y Google cargadas y en revisión de la plataforma | Diego | 13-nov |
| Kit de ventas y CS: one-pager por producto, FAQ de alcance y respuesta tipo "lo tenemos el 31-dic" | Diego + Fer | 16-nov |
| Prototipo navegable de Reloj (Figma) para demos | Carolina | Meta 20-nov; **límite 23-nov** para la demo del webinar |
| Conversación con Lucas (FitchUp) y Jimena (Worky) | Fer + Santiago | Semana del 16 y 23-nov |
| Registro del webinar en Zoom/Teams + calendario | Diego | **13-nov** (la pauta necesita el link) |

### F1: Lanzamiento (lunes 16 y martes 17-nov)
- **Lunes 16-nov (festivo):** arranca la pauta de registro al webinar (LinkedIn, Meta y Google). Las campañas se suben el viernes 13 para que pasen la revisión de las plataformas.
- **Clientes:**
  - Email de anuncio "Lapzo crece contigo: 3 nuevos productos" (segmentos A–D).
  - Banner in-app.
  - Mensaje de WhatsApp de cada CSM a sus contactos clave.
  - Invitación al webinar en todos los canales.
- **No clientes:**
  - Post de anuncio en LinkedIn de Lapzo + voceros (Santiago, Pedro, Fer) con el mismo mensaje.
  - Email a la base de leads.
- **Interno:** brief a todo Lapzo (ventas, CS, soporte) con alcance, FAQ y qué NO prometer, para evitar otro caso "pidieron demo de Reloj y no había".

### F2: Captación para el webinar (16 al 23-nov)
- Serie de contenido "Cuenta regresiva al 1 de enero": 3 posts esa semana (carrusel, encuesta y video corto con Lapzi); sigue después del webinar con 2 por semana.
- Pauta de registros al webinar (Meta + LinkedIn) y Search en Google con keywords de alta intención ("reloj checador", "registro electrónico de jornada", "control de asistencia empleados").
- Email de nurturing de GP el 19-nov y recordatorios del webinar (23 y 24-nov). El de Reclutamiento pasa al 26-nov, después del webinar.
- Ventana corta: son 8 días de captación, así que la mayor parte del presupuesto del webinar se gasta esa semana (ver §7).
- Ventas y CS usan el prototipo de Reloj en demos desde que Carolina lo libere.

### F3: Webinar y preventa (24-nov al 24-dic)
- **Webinar (martes 24-nov, 10:00 CDMX, 45 min + 15 de Q&A):** *"Registro electrónico de jornada 2027: lo que tu empresa debe tener listo el 1 de enero"*.
  - Agenda: la reforma en 10 minutos (invitado experto laboral, idealmente de un despacho o aliado), las 5 claves para prepararte, demo del prototipo de Reloj (Pedro) y oferta de lista prioritaria.
  - Hosts: Pedro Sors + invitado laboral; Diego modera.
- **Seguimiento:**
  - A las 24 h: grabación + one-pager.
  - Asistentes con intención alta van a Fer (nuevos) o al CSM (clientes) en < 24 h.
  - Los no asistentes reciben la grabación y entran a retargeting.
- **Preventa (25-nov al 24-dic):**
  - Secuencia "lista prioritaria": 3 emails + WhatsApp para clientes.
  - Mensaje: *"asegura tu habilitación en la primera ola de enero"*. El gancho comercial (precio early adopter, bundle o Comunidad de regalo) **queda pendiente de la propuesta de pricing**; el copy tiene la variable `[OFERTA]`.
  - Aprovechamos la ventana de cierre de presupuesto.
- **Pausa de pauta** del 24-dic al 4-ene (baja atención y CPM caro). Solo queda retargeting de bajo presupuesto.

### F4: Release Reloj Checador (31-dic) y anuncio "ya está aquí" (martes 5-ene)
- El 31-dic es jueves festivo de facto: el release es interno. El **anuncio externo es el 5-ene**.
- Contenido: *"Ya está aquí. El registro electrónico de jornada ya es obligatorio, y tú ya puedes tenerlo en Lapzo."*
- A la lista prioritaria, webinar, visitantes y clientes: email + WhatsApp + in-app, con agenda de habilitación.
- Retargeting a todas las audiencias de F2–F3.
- Landing de Reloj cambia de "Lista prioritaria" a "Agenda tu demo" (hay que activar la versión B de la landing).

### F5: Habilitación y adopción (6 al 31-ene)
- Onboarding de la primera ola de preventas (2.ª semana de enero).
- Primer caso de uso o testimonio de cliente de Reloj para fines de enero.
- Comunicar reportería cuando Producto la confirme.
- Retro de campaña el 30-ene: KPIs, aprendizajes e insumos para pricing y roadmap.

---

## 6. Canales y frecuencia

| Canal | Uso | Frecuencia | Dueño |
|---|---|---|---|
| **Email HubSpot** | Anuncio, nurturing por producto, webinar, preventa | 1–2 por semana por segmento (máx.) | Diego |
| **WhatsApp** | Clientes: mensaje 1:1 de CSM (no masivo frío). Leads: solo con opt-in del form | 17-nov, 23-nov (recordatorio), 9-dic (preventa), 5-ene | Vips / CSMs |
| **In-app (plataforma)** | Banner/aviso a admins de RH de clientes (vía Comunidad/anuncios) | 17 al 24-nov (webinar); 25-nov al 23-dic (lista prioritaria); 5-ene (Reloj ya está) | Diego + Producto |
| **LinkedIn orgánico** | Lapzo + voceros: anuncio, cuenta regresiva, recap de webinar | 3 posts/sem Lapzo; 1/sem por vocero | Diego + voceros |
| **Meta orgánico (IG/FB)** | Carruseles y reels con Lapzi (tono más cercano, Sofía) | 2 por semana | Diego |
| **Pauta** | Registros al webinar, lista prioritaria, retargeting | Ver §7 | Diego |
| **Ventas / CS** | Demo con prototipo, kit, seguimiento < 24 h | Continuo | Fer / Vips |

---

## 7. Presupuesto de pauta ($28,000 MXN)

| Canal | Objetivo | Monto | Periodo | Nota |
|---|---|---|---|---|
| **LinkedIn Ads** | Registros al webinar (Lead Gen Form), cargos RH/Dirección MX; después, lista prioritaria | $11,000 | $8,000 del 16 al 23-nov (webinar) + $3,000 del 25-nov al 18-dic | CPL esperado alto, pero es la audiencia exacta (Pedro, Santiago) |
| **Meta Ads** | Registros al webinar + lista prioritaria (Sofía) | $7,000 | $4,000 del 16 al 23-nov (webinar) + $3,000 del 25-nov al 23-dic | Lead form nativo + tráfico a landing |
| **Google Search** | Keywords de alta intención de Reloj | $6,000 | 16-nov al 23-dic y 5 al 31-ene | Concordancia de frase; negativas: "gratis", "app gratis", "biométrico" |
| **Retargeting (Meta + LinkedIn)** | Visitantes, registrados y engagement: "ya está aquí" | $4,000 | 25-nov al 23-dic y 5 al 20-ene | Audiencias excluyendo partners y clientes ya convertidos |
| **Total** | | **$28,000** | | Reserva de $2k para impulsar lo que mejor funcione |

Revisión semanal (lunes): se mueve presupuesto al canal con mejor CPL→SQL, no al de mejor CPL a secas.

---

## 8. Calendario detallado

| Fecha | Hito | Canal / acción |
|---|---|---|
| Jue 12-nov | Sesión de seguimiento: estrategia, artes y landings | Reunión 10:30 |
| Vie 13-nov | Aprobación de alcance de copys + lista de exclusión. Artes de pauta, forms, pixels y registro del webinar listos; campañas a revisión | Carolina / Vips / Diseño / Diego |
| **Lun 16-nov** | **Festivo. Arranca la pauta de registro al webinar**; QA de landings | LinkedIn + Meta + Google |
| **Mar 17-nov** | **Lanzamiento de la suite** + invitación al webinar | Email clientes y leads + in-app + WhatsApp CSM + LinkedIn |
| Mié 18-nov | Post: "Qué cambia el 1 de enero" (carrusel) + post de Pedro | LinkedIn + IG |
| Jue 19-nov | Email de nurturing: Gestión de Personal (con P.D. del webinar) | Email |
| ~Vie 20-nov | Prototipo de Reloj para demos (meta; límite 23-nov) | Carolina |
| Lun 23-nov | Recordatorio del webinar (email + WhatsApp a clientes con opt-in) | Email / WhatsApp / LinkedIn |
| **Mar 24-nov** | **Webinar Reloj Checador / reforma**, 10:00 CDMX | Zoom/Teams |
| Mié 25-nov | Grabación + one-pager; arranca preventa; la pauta pasa a lista prioritaria y retargeting | Email + pauta |
| Jue 26-nov | Email de nurturing: Reclutamiento | Email |
| Mar 1-dic | Preventa: email 1 | Email |
| Mié 9-dic | Preventa: email 2 + WhatsApp CSM | Email / WhatsApp |
| Mar 15-dic | Preventa: email 3 "últimos lugares de la primera ola" | Email |
| Jue 24-dic | Pausa de pauta (salvo retargeting mínimo) | — |
| Jue 31-dic | Release de Reloj Checador (interno) | Producto |
| **Mar 5-ene** | **Anuncio "Reloj Checador ya está aquí"** | Todos los canales + landing versión B |
| Mar 12-ene | Habilitación de la primera ola | Producto / CS |
| Vie 15-ene | Corte de KPIs: preventas y SQLs | Diego / Fer / Vips |
| Vie 30-ene | Retro de campaña | Todos |

---

## 9. Responsables (RACI simplificado)

| Frente | R (ejecuta) | A (aprueba) | C (consultado) |
|---|---|---|---|
| Estrategia, landings, pauta, email, orgánico | Diego | Vivian | Fer, Pedro |
| Alcance de producto en copys, prototipos, Figmas | Carolina | Carolina | Diego |
| Pricing y bundles (benchmark + propuesta) | Fer + Diego | Santiago / Pedro | Vivian |
| Partners (FitchUp, Worky) | Fer + Santiago | Santiago | Pedro |
| Comunicación a clientes y exclusiones | Vivian (CS) | Vivian | Diego |
| Renovación Tata | Pedro | Pedro | Fer |
| Webinar (contenido y demo) | Pedro (host) + Diego (moderación/producción) | Vivian | Carolina |
| Seguimiento de leads < 24 h | Fer (nuevos) / CSMs (clientes) | Fer / Vivian | Diego |

---

## 10. Riesgos y mitigación

| Riesgo | Impacto | Mitigación |
|---|---|---|
| **Estabilidad de plataforma** (incidente SSO/reportes/app del 3-nov, 17 clientes con casos) | Anunciar productos nuevos a clientes molestos resta credibilidad | Antes del envío del 17-nov, Vips confirma que los casos están cerrados. A las cuentas afectadas les llega primero un mensaje 1:1 de su CSM con la explicación del postmortem, y después el anuncio. Si hay otra crisis abierta el 16-nov, se pospone el email a clientes (no la pauta) |
| Pedir demo de Reloj y no tener qué mostrar (caso Larry) | Quedamos mal en ventas | Discurso único: "llega el 31-dic, te muestro cómo funcionará" + prototipo Figma. Hasta tenerlo, se usa la landing y el one-pager |
| Prometer de más (nómina, biométricos, firma digital) | Clientes insatisfechos, churn | Check de alcance de Carolina por pieza + FAQ interna de "qué NO decir" |
| Fricción con partners FitchUp / Worky | Pérdida de canal y de Tata | Exclusión global de listas y audiencias. Fer y Santiago hablan con ellos antes del 23-nov (antes del webinar). Mensajes sin atacar competidores |
| Pricing no definido al lanzar | Fricción en cotización | CTA "agenda demo / cotiza" sin precios; variable `[OFERTA]` en la preventa hasta la propuesta de Fer y Diego |
| Retraso del release del 31-dic | Preventas sin entrega | Comunicar "habilitación desde enero" (no día exacto). Plan B de comunicación preparado |
| Ventana de captación corta para el webinar (8 días, 16 al 23-nov) | No llegar a los 300 registros | Pauta concentrada esa semana, invitación a toda la base propia el 17-nov, voceros y WhatsApp de CSMs. Corte el viernes 20-nov: si vamos por debajo de 150, movemos la reserva de $2k a LinkedIn y Meta |
| Presupuesto bajo de pauta | Poco volumen externo | Apalancar base propia, voceros, webinar co-organizado con un aliado legal (su audiencia) y orgánico |
| Afirmaciones legales erróneas | Riesgo reputacional | Validar con legal o el invitado laboral: fechas (1-ene-2027 registro electrónico; 48 a 46 h en 2027; 40 h en 2030) y monto de multas antes de publicar |

---

## 11. Decisiones que necesito del equipo (sesión del jueves)

1. **Metas:** ¿validamos 60 SQLs (35 + 25) y 12 preventas de Reloj al 15-ene?
2. **Gancho de preventa `[OFERTA]`:** ¿precio early adopter congelado, bundle GP + Reloj con Comunidad de regalo, o solo prioridad de habilitación? Lo define la propuesta de pricing de Fer y Diego.
3. **Host del webinar:** ¿Pedro? ¿Conseguimos un invitado laboral externo (despacho o aliado) para el bloque de la reforma?
4. **Prototipo de Reloj:** fecha firme de Carolina para el Figma navegable (lo necesito a más tardar el 23-nov para la demo del webinar del 24-nov).
5. **Lista de exclusión FitchUp/Worky:** ¿quién la entrega y para cuándo? (Propuesta: Vips, 13-nov.)
6. **Firma de mensajes a clientes:** ¿va de Vips (CS), de Santiago (CEO) o de Lapzo genérico?
7. **Estado de la plataforma:** ¿confirmamos el 16-nov que los casos del incidente están cerrados antes del envío a clientes?
8. **Nombre comercial:** ¿"Gestión de Personal" o "Gestión de Personas"? En la sesión se usaron ambos. Recomiendo **"Gestión de Personal"** y uso ese en las piezas.

---

## 12. Fuentes sobre la reforma (validar antes de publicar)

- [El Imparcial: la jornada de 40 horas obligará a usar reloj checador a partir de 2027](https://www.elimparcial.com/mexico/2026/03/15/jornada-de-40-horas-no-beneficiara-a-todos-los-trabajadores-y-obligara-a-las-empresas-a-usar-el-reloj-checador-a-partir-de-2027-para-vigilar-las-horas-extra/)
- [El Imparcial: reloj checador obligatorio y multas de hasta 590 mil pesos](https://www.elimparcial.com/mexico/2026/04/14/la-nueva-jornada-laboral-de-40-horas-en-mexico-incluira-reloj-checador-obligatorio-y-multas-de-hasta-590-mil-pesos-para-empresas-que-incumplan/)
- [EY Law Flash: reducción de jornada laboral](https://www.ey.com/es_mx/technical/tax/boletines-fiscales/ey-law-flash-reduccion-jornada-laboral)
- [El Contribuyente: registro electrónico de asistencia que exige la reforma](https://www.elcontribuyente.mx/2026/10/registro-electronico-de-asistencia-que-exige-la-reforma-laboral/)
- [IDC Online: registro electrónico de jornada y contratos](https://idconline.mx/laboral/2026/08/28/registro-electronico-de-jornada-laboral-debo-actualizar-los-contratos-de-mis-trabajadores)
- [Greenberg Traurig: reforma a la LFT, reducción de jornada](https://www.gtlaw.com/en/insights/2026/5/reforma-a-la-ley-federal-del-trabajo---reduccion)
