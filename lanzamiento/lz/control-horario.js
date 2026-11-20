// Widget de Control Horario: los 6 estados del Figma "Control Horario · Componentes — Opción A + Notificaciones".
// render(estado) -> HTML del widget; navbtn(estado) -> botón del topnav; toast(estado) -> notificación.
(function () {
  const t = s => { const [h, m] = s.split(':').map(Number); return h * 60 + m; };
  // Segmentos de la barra: [tipo, desde, hasta] sobre una escala [ini, fin].
  const bar = (scale, segs, ticks) => {
    const [a, b] = scale.map(t), span = b - a;
    const parts = segs.map(([k, f, to, now]) => {
      const w = ((t(to) - t(f)) / span) * 100;
      return `<i class="${k}${now ? ' now' : ''}" style="width:${w.toFixed(2)}%"></i>`;
    }).join('');
    return `<div class="ch-bar" role="img" aria-label="Línea de tiempo de la jornada">${parts}</div>
      <div class="ch-ticks">${ticks.map(x => {
        const pct = Math.min(100, Math.max(0, ((t(x) - a) / span) * 100));
        const tr = pct < 6 ? '0' : pct > 94 ? '-100%' : '-50%';
        return `<span style="left:${pct.toFixed(2)}%;transform:translateX(${tr})">${x}</span>`;
      }).join('')}</div>`;
  };
  const cells = (arr, two) => `<div class="ch-grid${two ? ' two' : ''}">${arr.map(([l, v, live]) =>
    `<div class="ch-cell"><small>${l}</small><b${live ? ' class="live"' : ''}>${v}</b></div>`).join('')}</div>`;
  const list = rows => `<div class="ch-list">${rows.map(([l, v, x]) =>
    `<div><span>${l}</span><span>${v}${x ? ` <em>· ${x}</em>` : ''}</span></div>`).join('')}</div>`;
  const D1 = ['Descanso 1', '<b>12:13 - 12:23</b>', '10 min'];
  const D2 = ['Descanso 2', '<b>15:30 - 16:06</b>', '36 min'];
  const DAY = [['w', '08:57', '12:13'], ['b', '12:13', '12:23'], ['w', '12:23', '15:30'], ['b', '15:30', '16:06'], ['w', '16:06', '17:10']];

  const S = {
    idle: {
      label: 'Sin iniciar', nav: ['idle', 'Iniciar Jornada'], toast: 'Jornada iniciada a las 08:57',
      html: () => cells([['Hora actual', '08:40'], ['Tiempo trabajado', '0m'], ['Descanso', '0m']]) +
        bar(['09:00', '18:00'], [], ['09:00', '14:00', '18:00']) +
        `<div class="ch-note">Tu turno es de 09:00 a 18:00</div><div class="ch-btns"><span class="ch-btn">Iniciar jornada</span></div>`
    },
    work: {
      label: 'Trabajando', nav: ['work', '05:23:14'], toast: 'Descanso iniciado a las 15:30',
      html: () => cells([['Hora actual', '15:42'], ['Tiempo trabajado', '5h 23m', 1], ['Descanso', '10m']]) +
        bar(['09:00', '18:00'], [['w', '09:00', '12:13'], ['b', '12:13', '12:23'], ['w', '12:23', '15:42']], ['09:00', '13:30', '18:00']) +
        list([['Entrada', '<b>08:57</b>'], D1, ['Salida', '<span class="pend">Pendiente</span>']]) +
        `<div class="ch-btns"><span class="ch-btn">Iniciar descanso</span><span class="ch-btn o">Finalizar jornada</span></div><span class="ch-link">Solicitar corrección</span>`
    },
    break: {
      label: 'En descanso', nav: ['break', '00:12:08'], toast: 'Bienvenido de vuelta. Descanso de 36 min registrado.',
      html: () => cells([['Hora actual', '15:42'], ['Tiempo trabajado', '6h 23m'], ['Descanso', '46m', 1]]) +
        bar(['09:00', '18:00'], [['w', '09:00', '12:13'], ['b', '12:13', '12:23'], ['w', '12:23', '15:30'], ['b', '15:30', '15:42', 1]], ['09:00', '13:30', '18:00']) +
        list([['Entrada', '<b>08:57</b>'], D1, ['Descanso 2', '<b>15:30</b>', '<span class="now">En curso</span>'], ['Salida', '<span class="pend">Pendiente</span>']]) +
        `<div class="ch-btns"><span class="ch-btn">Terminar descanso</span></div><span class="ch-link">Solicitar corrección</span>`
    },
    confirm: {
      label: 'Confirmar cierre', nav: ['done', '07:27:39'], toast: 'Jornada finalizada. Trabajaste 7h 27m',
      html: () => `<div class="ch-title"><b>Confirma antes de cerrar</b><small>Lunes 10 oct · Turno 09:00 - 18:00</small></div>` +
        cells([['Entrada', '08:57'], ['Salida', '17:10'], ['Tiempo trabajado', '7 h 27m'], ['Descansos', '46m']], 1) +
        bar(['08:57', '18:00'], DAY, ['09:00', '13:30', '18:00']) +
        list([['Entrada', '<b>08:57</b>'], D1, D2, ['Salida', '<b>17:10</b>']]) +
        `<div class="ch-btns"><span class="ch-btn">Sí, todo está correcto</span></div><span class="ch-link">Solicitar corrección</span>`
    },
    done: {
      label: 'Jornada finalizada', nav: ['done', '07:27:39'], toast: null,
      html: () => `<span class="ch-badge">✓ Jornada finalizada</span>` +
        cells([['Entrada', '08:57'], ['Salida', '17:10'], ['Tiempo trabajado', '7 h 27m'], ['Descansos', '46m']], 1) +
        bar(['08:57', '18:00'], DAY, ['09:00', '13:30', '18:00']) +
        list([['Entrada', '<b>08:57</b>'], D1, D2, ['Salida', '<b>17:10</b>']]) +
        `<div class="ch-note" style="color:#d9dbe9">Nos vemos mañana. Tu próximo turno empieza a las 09:00.</div>`
    },
    extra: {
      label: 'Horas extra', nav: ['done', '09:14:02'], toast: 'Jornada finalizada. 1h 00m fuera de turno registrada',
      html: () => `<div class="ch-title"><b>Confirma antes de cerrar</b><small>Lunes 10 oct · Turno 09:00 - 18:00</small></div>` +
        cells([['Entrada', '08:57'], ['Salida', '19:00'], ['Tiempo trabajado', '9 h 14m'], ['Descansos', '46m']], 1) +
        bar(['08:57', '19:00'], [...DAY.slice(0, 4), ['w', '16:06', '18:00'], ['x', '18:00', '19:00']], ['09:00', '13:30', '18:00']) +
        list([['Entrada', '<b>08:57</b>'], D1, D2, ['Salida', '<b>19:00</b>']]) +
        `<div class="ch-btns"><span class="ch-btn">Sí, todo está correcto</span></div><span class="ch-link">Solicitar corrección</span>`
    }
  };

  const widget = k => `<div class="ch" data-state="${k}">${S[k].html()}</div>`;
  const navbtn = k => {
    const [s, txt] = S[k].nav;
    return `<span class="navbtn" data-s="${s}">${s === 'idle' ? '' : '<span class="clk"></span>'}${txt}</span>`;
  };
  const toast = k => S[k].toast
    ? `<div class="toast" role="status"><span class="ico check"></span><span>${S[k].toast}</span><span class="ico close"></span></div>` : '';

  // Monta un escenario: [data-ch-stage] con hijos [data-ch-widget], [data-ch-nav], [data-ch-toast]
  // y controles [data-ch-go="estado"]. data-autoplay="ms" lo recorre solo (se pausa con hover/foco).
  function mount(root) {
    const order = (root.dataset.order || 'idle,work,break,confirm,done').split(',');
    const w = root.querySelector('[data-ch-widget]'), n = root.querySelector('[data-ch-nav]'), ts = root.querySelector('[data-ch-toast]');
    const ctrls = [...root.querySelectorAll('[data-ch-go]')];
    let i = 0, timer = null, paused = false;
    const show = k => {
      i = order.indexOf(k);
      if (w) w.innerHTML = widget(k);
      if (n) n.innerHTML = navbtn(k);
      // La notificación confirma la acción que llevó a este estado (la del estado anterior).
      if (ts) { const prev = order[i - 1]; ts.innerHTML = prev ? toast(prev) : ''; }
      ctrls.forEach(c => { const on = c.dataset.chGo === k; c.classList.toggle('on', on); c.setAttribute('aria-pressed', on); });
    };
    ctrls.forEach(c => c.addEventListener('click', () => { show(c.dataset.chGo); restart(); }));
    const ms = +root.dataset.autoplay || 0;
    const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
    const restart = () => {
      clearInterval(timer);
      if (ms && !reduce) timer = setInterval(() => { if (!paused) show(order[(i + 1) % order.length]); }, ms);
    };
    root.addEventListener('mouseenter', () => paused = true);
    root.addEventListener('mouseleave', () => paused = false);
    root.addEventListener('focusin', () => paused = true);
    root.addEventListener('focusout', () => paused = false);
    show(root.dataset.start || order[0]);
    restart();
  }
  document.querySelectorAll('[data-ch-stage]').forEach(mount);
})();
