// Comportamiento compartido de las landings del lanzamiento.

// Tabs de personas
document.querySelectorAll('.tab').forEach(tab => tab.addEventListener('click', () => {
  document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
  document.querySelectorAll('.panel').forEach(p => p.classList.remove('active'));
  tab.classList.add('active');
  document.getElementById('panel-' + tab.dataset.tab).classList.add('active');
}));

// Formularios: placeholder hasta reemplazar por el embed de HubSpot.
document.querySelectorAll('form.lead').forEach(f => f.addEventListener('submit', e => {
  e.preventDefault();
  f.classList.add('sent');
  f.querySelector('button').disabled = true;
}));

// Cuenta regresiva al 1-ene-2027 (registro electrónico de jornada).
const cd = document.querySelector('[data-countdown]');
if (cd) {
  const target = new Date(cd.dataset.countdown).getTime();
  const tick = () => {
    const ms = Math.max(0, target - Date.now());
    const d = Math.floor(ms / 864e5), h = Math.floor(ms / 36e5) % 24, m = Math.floor(ms / 6e4) % 60;
    cd.querySelector('[data-d]').textContent = d;
    cd.querySelector('[data-h]').textContent = String(h).padStart(2, '0');
    cd.querySelector('[data-m]').textContent = String(m).padStart(2, '0');
  };
  tick(); setInterval(tick, 30000);
}

// Fase de campaña: antes / después del anuncio "ya está aquí" (5-ene-2027).
// Forzar con ?fase=post para revisar la versión B.
const LAUNCH = new Date('2027-01-05T00:00:00-06:00').getTime();
const fase = new URLSearchParams(location.search).get('fase');
if (fase === 'post' || (fase !== 'pre' && Date.now() >= LAUNCH)) {
  document.documentElement.classList.add('post-launch');
  document.querySelectorAll('[data-post]').forEach(el => { el.innerHTML = el.dataset.post; });
}

// Después del webinar (martes 24-nov, 11:00 CDMX) la sección pasa a "grabación". Forzar con ?fase=grabacion.
const WEBINAR_END = new Date('2026-11-24T11:00:00-06:00').getTime();
if (fase === 'grabacion' || fase === 'post' || (fase !== 'pre' && Date.now() >= WEBINAR_END)) {
  document.documentElement.classList.add('post-webinar');
  document.querySelectorAll('[data-pw]').forEach(el => { if (!document.documentElement.classList.contains('post-launch')) el.innerHTML = el.dataset.pw; });
}
