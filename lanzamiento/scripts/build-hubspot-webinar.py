#!/usr/bin/env python3
"""Genera la plantilla HubL de la landing del webinar (webinar-reloj.html) para HubSpot.

- Incrusta CSS, imágenes y las fuentes Degular (Poppins se carga de Google Fonts).
- Sustituye el form de muestra por el form de HubSpot ({% form %}).
- Agrega el Meta Pixel (Lernit Pixel) con PageView y Lead al enviar el form, más dataLayer.

Uso: python3 lanzamiento/scripts/build-hubspot-webinar.py OUT.html [FORM_GUID]
Sin FORM_GUID se deja un módulo de form editable para elegir el form en el editor de HubSpot."""
import importlib.util, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('bs', HERE / 'build-standalone.py')
bs = importlib.util.module_from_spec(spec); spec.loader.exec_module(bs)

PIXEL_ID = '337850720804196'          # Lernit Pixel (cuenta Lernit - Lapzo)
CONTENT_NAME = 'Webinar Registro de jornada 2027 (1-dic)'

TRACKING = """
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap">
<!-- Meta Pixel: Lernit Pixel. Si el portal ya lo carga en el header global, no se vuelve a inicializar. -->
<script>
(function(){
  var ID='%(pid)s';
  if(!window.fbq){
    !function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?n.callMethod.apply(n,arguments):n.queue.push(arguments)};
    if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;
    t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}(window,document,'script','https://connect.facebook.net/en_US/fbevents.js');
    fbq('init',ID);
  }
  fbq('track','PageView');
  fbq('trackCustom','ViewWebinarLanding',{content_name:'%(cn)s'});
  window.dataLayer=window.dataLayer||[];
  var sent=false;
  window.lzLead=function(src){
    if(sent)return; sent=true;
    var eid='lead-'+Date.now()+'-'+Math.random().toString(36).slice(2,8);
    fbq('track','Lead',{content_name:'%(cn)s',content_category:'webinar',currency:'MXN',value:0},{eventID:eid});
    window.dataLayer.push({event:'webinar_registro',form_source:src||'hubspot',event_id:eid});
  };
  // Form clásico de HubSpot (postMessage) y form del editor nuevo (evento del DOM).
  window.addEventListener('message',function(e){
    if(e.data&&e.data.type==='hsFormCallback'&&e.data.eventName==='onFormSubmitted')window.lzLead('hs-legacy');
  });
  window.addEventListener('hs-form-event:on-submission:success',function(){window.lzLead('hs-v4');});
})();
</script>
<noscript><img height="1" width="1" style="display:none" src="https://www.facebook.com/tr?id=%(pid)s&ev=PageView&noscript=1"/></noscript>
""" % {'pid': PIXEL_ID, 'cn': CONTENT_NAME}

def form_tag(guid):
    msg = '¡Listo! Te enviamos el enlace de acceso a tu correo.'
    if guid:
        return ('{%% form "registro_webinar" form_to_use="%s", response_response_type="inline", '
                'response_message="%s", label="Formulario de registro" %%}' % (guid, msg))
    return '{%% form "registro_webinar" response_response_type="inline", response_message="%s", label="Formulario de registro" %%}' % msg

TEXT = (''.join(chr(c) for c in range(0x20, 0x7f)) + 'áéíóúüñÁÉÍÓÚÜÑ¡¿·–—“”‘’…')

def optimized(path):
    """Versión ligera de un asset para que la plantilla HubL pese poco (el límite práctico es el tamaño de la llamada)."""
    import base64, io
    if path.name.startswith('Degular-'):
        from fontTools import subset
        from fontTools.ttLib import TTFont
        f = TTFont(str(path)); opts = subset.Options(); opts.flavor = 'woff2'; opts.layout_features = ['kern', 'liga']
        sub = subset.Subsetter(opts); sub.populate(text=TEXT); sub.subset(f)
        buf = io.BytesIO(); f.flavor = 'woff2'; f.save(buf)
        return 'data:font/woff2;base64,' + base64.b64encode(buf.getvalue()).decode()
    if path.suffix.lower() == '.png':
        from PIL import Image
        im = Image.open(path).convert('RGBA'); im.thumbnail((180, 180))
        buf = io.BytesIO(); im.save(buf, 'WEBP', quality=80)
        return 'data:image/webp;base64,' + base64.b64encode(buf.getvalue()).decode()
    return _uri(path)

_uri = bs.uri

def main():
    out = pathlib.Path(sys.argv[1]); guid = sys.argv[2] if len(sys.argv) > 2 else ''
    bs.FONT_KEEP = r'Degular-Bold'
    bs.uri = optimized
    html = bs.build_html('webinar-reloj.html')
    # Un solo archivo de Degular (Bold) sirve también para el peso 600.
    html = html.replace('format("opentype");font-weight:700', 'format("woff2");font-weight:600 700')
    html = re.sub(r'<!--HS_FORM-->.*?<!--/HS_FORM-->', lambda m: form_tag(guid), html, flags=re.S)
    html = html.replace('<!--TRACKING-->', TRACKING)
    html = html.replace('</head>', '{{ standard_header_includes }}\n</head>', 1)
    html = html.replace('</body>', '{{ standard_footer_includes }}\n</body>', 1)
    # El form de muestra local ya no existe; quitar su manejador.
    html = re.sub(r"\s*// Vista local:.*?\n.*?\}\); \}\);", '', html)
    out.write_text(html, encoding='utf-8')
    print(out, round(len(html.encode()) / 1024), 'KB')

if __name__ == '__main__':
    main()
