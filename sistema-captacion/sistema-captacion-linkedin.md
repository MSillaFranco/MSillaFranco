# Sistema de captación de clientes en LinkedIn con Claude

Ochin Kraso · versión 1 · 5 de noviembre de 2026

Regla de oro: Claude investiga, redacta y ordena. Mariano publica, envía y firma. Ningún mensaje ni publicación sale sin confirmación expresa.

---

## Mapa del sistema

| Paso | Frecuencia | Qué hace Claude | Qué haces tú | Tiempo tuyo |
|---|---|---|---|---|
| 1. Cliente ideal | Trimestral | Propone y afina perfiles | Validas con conversaciones reales | 2 h |
| 2. Contenido | Semanal | Busca, verifica y redacta | Revisas y publicas | 3 h |
| 3. Señales | Diaria | Clasifica y prioriza | Anotas interacciones | 15 min |
| 4. Primer contacto | Diaria | Redacta borradores personalizados | Envías a mano | 15 min |
| 5. Seguimiento | Según agenda | Prepara reunión y propuesta | Llevas la reunión y cierras | Variable |
| 6. Medición | Mensual | Resume y detecta patrones | Decides qué repetir | 1 h |

Los tiempos son una estimación de partida, no un dato medido. Ajústalos tras el primer mes.

---

## Paso 1. Cliente ideal

### Plantilla de ficha (una por perfil, máximo tres)

```
PERFIL: [nombre corto, p. ej. "Responsable de RR. HH. en despliegue de IA"]
Cargo y área:
Tamaño y sector de la empresa:
Situación actual con la IA: [prohibida / uso sin control / piloto / despliegue]
Problema que le quita el sueño:
Qué ha intentado ya:
Qué le haría quedar bien ante su dirección:
Quién decide y quién paga:
Señales en LinkedIn: [qué temas comenta, qué publica]
Servicio de Ochin Kraso que encaja: [formación / taller / asesoría / charla]
Frase que usaría para describir su problema:
```

### Prompt para Claude

```
Actúa como estratega comercial para un divulgador y formador en gobernanza
de IA en España (Ochin Kraso). Propón tres perfiles de cliente ideal con la
plantilla adjunta. Prioriza organizaciones que ya usan IA sin reglas claras.
Para cada perfil, indica qué dato habría que confirmar con una conversación
real antes de darlo por bueno. No inventes estadísticas.
```

### Validación
Tres conversaciones por perfil antes de dar la ficha por buena. Pregunta clave: "¿Qué te preocupa hoy de cómo se usa la IA en tu equipo?".

---

## Paso 2. Contenido que atrae

### Calendario semanal

| Día | Pieza | Objetivo |
|---|---|---|
| Martes | Criterio: tendencia analizada con el marco quién actúa, quién responde, qué norma aplica | Autoridad |
| Jueves | Plantilla o herramienta descargable (política, checklist, lámina) | Conversaciones |
| Sábado o domingo | Substack: desarrollo largo de la pieza del martes | Profundidad y GEO |

### Flujo de producción (el que ya usamos)

1. Claude busca tendencias de fondo en tu campo.
2. Eliges una.
3. Claude la pasa por la aduana de afirmaciones.
4. Claude redacta los borradores de LinkedIn y Substack, la imagen, el texto alternativo y el primer comentario.
5. Revisas, ajustas y publicas.

### Llamada a la acción que capta (en lugar de "sígueme")

- "Si quieres la plantilla completa, escribe PLANTILLA en comentarios y te la paso."
- "¿Te la mando en formato editable? Dímelo por mensaje."

La plantilla no se entrega por un enlace público en el post: se entrega por mensaje privado, y así se abre la conversación.

---

## Paso 3. Señales de interés

### Hoja de seguimiento

Archivo: `seguimiento-senales.csv` (en esta misma carpeta). Columnas:

| Columna | Qué apuntar |
|---|---|
| fecha | Día de la señal |
| nombre | Nombre de la persona |
| cargo | Cargo visible en su perfil |
| empresa | Empresa |
| perfil_cliente | Perfil del paso 1 que encaja (o "ninguno") |
| senal | comentario / guardado / compartido / visita perfil / mensaje / petición de plantilla |
| contenido_origen | Qué publicación lo provocó |
| lo_que_dijo | Resumen breve de su comentario (si lo hay) |
| prioridad | alta / media / baja (la propone Claude, la decides tú) |
| estado | pendiente / contactado / conversación / reunión / propuesta / cliente / descartado |
| siguiente_paso | Qué toca y cuándo |
| notas | Libre |

### Prompt diario

```
Te paso las señales de hoy de mi hoja de seguimiento. Para cada fila:
1. Asigna el perfil de cliente que mejor encaja (o "ninguno").
2. Propón prioridad (alta, media, baja) y explica el motivo en una línea.
3. Indica si conviene escribir hoy, esperar o no escribir.
Usa solo la información de la hoja. No supongas datos que no estén.
```

### Criterio de prioridad (orientativo)

- **Alta:** encaja en un perfil y ha pedido algo o ha hecho una pregunta.
- **Media:** encaja en un perfil y ha comentado con contenido.
- **Baja:** reacción sin comentario o perfil que no encaja.

---

## Paso 4. Primer contacto

### Normas

- Lo envías tú, a mano. Nada de herramientas que automaticen mensajes, invitaciones o extraigan perfiles: las condiciones de uso de LinkedIn lo prohíben y es la vía rápida para perder la cuenta.
- Ritmo sostenible: pocos mensajes y buenos al día, mejor que muchos genéricos.
- Primer mensaje sin venta. Se aporta algo útil.
- Máximo un recordatorio si no hay respuesta, a los 7 días. Después, se deja.

### Plantillas (Claude las personaliza; tú revisas)

**A. Ha comentado una publicación**
```
Hola, [nombre]. Gracias por tu comentario sobre [tema]. Me quedé con lo de
[detalle concreto de su comentario]. Tengo una plantilla de [recurso] que
desarrolla justo ese punto. ¿Te la paso?
```

**B. Ha pedido la plantilla**
```
Hola, [nombre]. Aquí la tienes: [recurso]. Está pensada para [uso]. Si la
aplicas en [empresa o sector], me interesa saber qué te encuentras: suele
fallar en [punto habitual].
```

**C. Ha visitado tu perfil y encaja**
```
Hola, [nombre]. He visto que trabajas en [área] en [empresa]. Estoy
publicando sobre [tema relacionado con su área]. Si te resulta útil, te
paso la plantilla de [recurso].
```

**D. Recordatorio (una sola vez)**
```
Hola, [nombre]. Te dejo de nuevo [recurso] por si se perdió el mensaje.
Sin compromiso.
```

**E. Paso a conversación (cuando hay respuesta e interés)**
```
Me alegra que te sirva. Si quieres, lo vemos 20 minutos y te cuento cómo lo
están aplicando otras organizaciones. ¿Te viene bien [dos opciones de día]?
```

En la plantilla E no prometas casos que no puedas citar. Si aún no tienes, usa "cómo lo aplicaría en tu caso".

### Prompt de personalización

```
Redacta un primer mensaje de LinkedIn para [nombre], [cargo] en [empresa].
Señal: [lo que hizo]. Lo que dijo: [texto]. Usa la plantilla [A/B/C].
Máximo 60 palabras, tuteo, español de España, sin emojis, sin halagos y sin
vender. Menciona un detalle concreto de su comentario. Dame dos versiones.
```

---

## Paso 5. Seguimiento y cierre

### Guion de conversación (20 minutos)

| Minutos | Bloque | Pregunta guía |
|---|---|---|
| 0-3 | Contexto | "¿Cómo se está usando la IA hoy en tu equipo?" |
| 3-10 | Problema | "¿Qué te preocupa más: datos, errores, cumplimiento, adopción?" |
| 10-14 | Consecuencias | "¿Qué pasa si sigue así seis meses más?" |
| 14-18 | Encaje | "Lo que suelo hacer en estos casos es [servicio]. ¿Encaja?" |
| 18-20 | Siguiente paso | "¿Te preparo una propuesta para [fecha]?" |

### Estructura de propuesta de formación

1. Situación de partida (con sus palabras).
2. Objetivo medible de la formación.
3. Contenido por módulos.
4. Formato, duración y número de personas.
5. Entregables (plantillas, política, checklist).
6. Inversión y condiciones.
7. Siguiente paso y fecha.

### Prompt de preparación

```
Prepara la reunión con [nombre] de [empresa], sector [sector]. Con lo que te
paso de la hoja y de sus comentarios, dame: tres preguntas adaptadas al
guion, los dos riesgos de gobernanza más probables en su sector y una
propuesta de formación con la estructura de siete puntos. Señala qué es
inferencia y qué es dato.
```

---

## Paso 6. Medición

### Indicadores mensuales

| Indicador | Cómo se calcula |
|---|---|
| Señales registradas | Filas nuevas en la hoja |
| Conversaciones iniciadas | Estado "conversación" o posterior |
| Reuniones | Estado "reunión" o posterior |
| Propuestas | Estado "propuesta" o posterior |
| Clientes | Estado "cliente" |
| Contenido que más convierte | Publicación de origen de las reuniones |

No hay cifras de referencia fiables para comparar. Compara cada mes contigo mismo.

### Prompt mensual

```
Analiza mi hoja de seguimiento del último mes. Dame: los indicadores de la
tabla, los tres contenidos que más conversaciones generaron, el perfil de
cliente que mejor responde y una recomendación concreta para el mes que
viene. Distingue dato de inferencia.
```

---

## Gobernanza del propio sistema

- **Confirmación:** Claude no publica ni envía nada. Todo queda en borrador.
- **Datos personales:** la hoja contiene datos de personas. Apunta solo lo necesario (lo que es visible en su perfil y lo que te han dicho), no datos sensibles, y borra a quien descartes o te lo pida. Si vas a escalar el sistema, revisa la base legal y el aviso de privacidad con un asesor de protección de datos.
- **Normas de LinkedIn:** sin automatización de mensajes, invitaciones ni extracción de perfiles.
- **Verificación:** todo contenido con cifras pasa por la aduana de afirmaciones antes de publicar.
- **Honestidad comercial:** no se citan clientes, casos ni resultados que no existan.
