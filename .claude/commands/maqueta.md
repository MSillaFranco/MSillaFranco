---
description: Genera maquetas de LinkedIn (post y carrusel) y Substack (cabecera, artículo y email) a partir de un texto
argument-hint: <ruta-del-texto o texto pegado>
---

Actúa como diseñador editorial y maquetador web para la marca Ochin Kraso.

OBJETIVO
A partir del texto de entrada, genera maquetas visuales realistas de cómo se vería
la pieza publicada en LinkedIn y en Substack. Son borradores internos para revisar.
No publiques nada ni te conectes a ninguna plataforma.

ENTRADA
- Texto fuente: $ARGUMENTS
  (si es una ruta, lee el archivo; si es texto, úsalo tal cual; si está vacío, pídemelo)
- Idioma: español de España.
- Autor: Mariano · Ochin Kraso · "Estratega en IA y gobernanza".
- Foto de perfil: si existe ./assets/avatar.png úsala; si no, un círculo con las iniciales MS.

PASO 1. ADAPTACIÓN DEL TEXTO (sin inventar datos)
Del texto fuente, extrae y adapta:
a) Post de LinkedIn: gancho en las 2 primeras líneas (que funcionen solas antes del
   corte "...ver más"), cuerpo en párrafos de 1 a 3 líneas, cierre con una pregunta o
   idea fuerza, 3 hashtags como máximo. Sin emojis.
b) Carrusel de LinkedIn: de 6 a 8 diapositivas. Portada con la tesis, una idea por
   diapositiva, una plantilla o esquema reutilizable y una diapositiva final con la
   llamada a la acción.
c) Artículo de Substack: título, subtítulo, cuerpo con secciones H2, un bloque de cita
   destacada y un cierre que invite a suscribirse.
No añadas cifras, citas ni fuentes que no estén en el texto. Si falta algo, márcalo
como [PENDIENTE: ...].

PASO 2. MAQUETAS (HTML + CSS, autocontenidas, sin dependencias externas)
Crea la carpeta ./maquetas/<slug-del-titulo>/ con:
1. linkedin-post.html     -> la tarjeta del post en el feed (cabecera con avatar,
   nombre y titular, el texto truncado con "...ver más", la imagen asociada y la barra
   de reacciones de muestra). Haz también una versión desplegada.
2. linkedin-carrusel.html -> cada diapositiva a 1080x1350 px.
3. substack-cabecera.html -> la imagen de cabecera del artículo, apaisada.
4. substack-articulo.html -> la vista del artículo en web (título, subtítulo, autor,
   fecha, cuerpo con tipografía serif, cita destacada y botón de suscripción).
5. substack-email.html    -> la vista de la newsletter en el correo, a 600 px de ancho.
6. textos.md              -> todos los textos finales listos para copiar y pegar.

Estilo visual de Ochin Kraso:
- Paleta: fondo #F7F5F0, texto #1A1A1A, acento #C2410C, gris secundario #6B6B6B
  (cámbiala aquí cuando tengas la definitiva).
- Tipografía: sans para LinkedIn y serif para el cuerpo de Substack (fuentes del
  sistema, sin cargar nada de fuera).
- Sobrio, con mucho aire, jerarquía clara y sin adornos.
- Las maquetas imitan la estructura de cada plataforma, pero no usan sus logotipos.

PASO 3. EXPORTACIÓN Y REVISIÓN
- Con Playwright (ya instalado), saca una captura PNG de cada HTML con
  deviceScaleFactor 2 y guárdala en ./maquetas/<slug>/png/.
- Exporta el carrusel también como un único PDF (formato nativo para el carrusel
  en LinkedIn).
- Revisa las capturas tú mismo y corrige lo que encuentres: texto cortado, contraste
  bajo, diapositivas con más de 40 palabras, o un gancho que no se entiende antes del
  corte "...ver más".

PASO 4. INFORME FINAL (breve)
- La lista de archivos generados.
- Los [PENDIENTE] que tengo que resolver yo.
- Dos variantes alternativas del gancho de LinkedIn y del título de Substack.
- Las medidas y límites que has usado. Marca cuáles has comprobado en una fuente
  oficial y cuáles son una convención o una estimación.
