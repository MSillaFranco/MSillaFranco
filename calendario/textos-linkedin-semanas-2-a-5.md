# Textos LinkedIn · semanas 2 a 5 (borradores, no publicados)

Todo dato marcado [VERIFICAR] debe pasar por la aduana de afirmaciones antes de publicar. Si no se confirma, se quita la frase; el texto está escrito para sostenerse sin ella.

---

## Mar 10 nov · IA física

El robot ya está en la fábrica. El responsable, todavía no.

Durante tres años hemos discutido qué hace la IA en una pantalla. Ahora empieza a tener brazos, ruedas y turnos de trabajo.

BMW, Toyota y Schaeffler están probando o contratando robots humanoides para mover cajas y cargar piezas [VERIFICAR alcance de cada caso]. No es ciencia ficción, pero tampoco es la revolución que venden los vídeos: son pilotos pequeños con tareas muy acotadas.

Lo interesante no es el robot. Es la pregunta que trae debajo del brazo.

Cuando un chatbot se equivoca, te da una respuesta mala. Cuando un robot se equivoca, tira un palé, golpea una máquina o hiere a alguien.

Y ahí la cadena de responsables se alarga:
- quien fabrica el robot,
- quien entrena el modelo que lo mueve,
- quien lo integra en la línea,
- quien decide en qué turno trabaja y junto a quién.

Europa ya ha puesto fecha a la IA integrada en productos: agosto de 2028, tras el aplazamiento del Digital Omnibus [VERIFICAR]. Hoy mismo, por cierto, el AI Act empieza a aplicarse en Irlanda del Norte, pero solo a la IA integrada en productos físicos [VERIFICAR si la decisión se confirmó].

La pregunta para cualquier director de planta no es si el robot es capaz. Es quién firma la evaluación de riesgos del puesto que comparte con una persona.

¿En tu sector, quién debería firmarla?

#IAFísica #Robótica #GobernanzaIA #PRL

---

## Jue 12 nov · Plantilla IA física

7 preguntas antes de meter un robot con IA en tu planta

Guárdalas. Si no puedes contestar alguna, el robot espera.

1. ¿Qué tarea exacta hace y cuál no puede hacer nunca?
2. ¿Quién es el responsable con nombre y apellido?
3. ¿Qué pasa si falla la conexión o el modelo: se para o sigue?
4. ¿Se ha rehecho la evaluación de riesgos del puesto con el robot dentro?
5. ¿Qué datos graba (vídeo, voz, movimientos de las personas) y quién los ve?
6. ¿Qué dice el contrato con el fabricante sobre actualizaciones y errores?
7. ¿Cómo se ha informado y formado a la plantilla que trabaja a su lado?

La séptima es la que más se olvida y la que más problemas evita.

¿Añadirías una octava?

#IAFísica #GobernanzaIA #Industria

---

## Mar 17 nov · Energía

Cada respuesta de IA tiene una factura de luz. España ha empezado a decidir quién la paga.

Solemos hablar de la IA como si fuera aire. Es cobre, agua, terreno y megavatios.

El Gobierno ha publicado un informe que advierte de que una expansión sin control de los centros de datos puede encarecer la factura eléctrica y aumentar las emisiones [VERIFICAR fecha y documento]. Su propuesta va más allá de pedir buena voluntad: plantea que la energía que consuman sea renovable nueva y que se case hora a hora con su consumo, con sanciones si no se cumple [VERIFICAR].

Traducido: no vale con comprar certificados verdes a final de año. Habría que demostrar que, a las 3 de la madrugada, tu centro de datos también funciona con energía limpia.

Por qué importa fuera del sector eléctrico:
- El coste de la IA que usas en la oficina acabará reflejando estas reglas.
- La pregunta "¿dónde se procesa?" deja de ser técnica y pasa a ser de reputación.
- Y vuelve una pregunta incómoda: ¿necesitamos el modelo más grande para resumir un correo?

La gobernanza de la IA también se escribe en el BOE de la energía.

#IA #Energía #CentrosDeDatos #GobernanzaIA

---

## Jue 19 nov · Plantilla IA local

¿Nube o en local? Árbol de decisión para la IA de tu oficina

Los modelos pequeños ya funcionan en un portátil normal. Eso cambia una decisión que casi nadie se está planteando.

Pregunta 1. ¿La tarea usa datos personales, de clientes o confidenciales?
- No: nube con un proveedor aprobado.
- Sí: pasa a la 2.

Pregunta 2. ¿Puedes anonimizarlos sin perder utilidad?
- Sí: nube con datos anonimizados.
- No: pasa a la 3.

Pregunta 3. ¿La tarea necesita el modelo más potente (razonamiento largo, mucho contexto)?
- No: modelo local.
- Sí: nube con contrato que garantice no reutilizar los datos, ubicación en la UE y registro. Revisión jurídica.

Lo innovador no es el modelo local. Es que, por primera vez, la privacidad no exige renunciar a la IA.

¿Tu empresa ya distingue qué tareas no pueden salir del ordenador?

#IALocal #RGPD #GobernanzaIA #Privacidad

---

## Mar 24 nov · Modelos del mundo

Los coches autónomos ya aprenden en mundos que no existen. ¿Quién certifica la simulación?

Hay una rama de la IA que no escribe ni dibuja: imagina. Se llaman modelos del mundo y generan entornos simulados en los que un coche o un robot puede practicar millones de veces lo que sería peligroso o carísimo probar en la calle.

Waymo ya usa uno basado en Genie 3, de Google DeepMind, para simular conducción [VERIFICAR]. Nvidia ha publicado Cosmos 3 con pesos abiertos para entrenar robots [VERIFICAR].

La ventaja es evidente. El riesgo, menos:

Si el robot aprende en un mundo simulado, su comportamiento en el mundo real depende de lo bien que ese simulador se parezca a la realidad. ¿Y quién comprueba eso?

No he encontrado una norma específica que obligue a validar los simuladores [inferencia: VERIFICAR antes de afirmarlo]. Hoy lo validan las propias empresas.

Es la misma lección de siempre, en otra escala: quien diseña el examen no debería ser el único que lo corrige.

#ModelosDelMundo #IAFísica #GobernanzaIA

---

## Jue 26 nov · IA científica

Solo 2 de 26 "científicos de IA" comprobaron sus hallazgos en un laboratorio real.

Es el dato de una revisión académica sobre agentes que investigan solos: generan hipótesis, diseñan experimentos e interpretan resultados [VERIFICAR cifra y fuente en arXiv]. La mayoría se evalúan con revisores automáticos o con sus propias pruebas.

Parece un problema de laboratorio. Es un problema de oficina.

Cada vez que un agente redacta un informe y luego "lo revisa", ocurre lo mismo: el sistema se corrige a sí mismo y nadie de fuera lo comprueba.

Tres reglas que sirven igual en un laboratorio que en un departamento:
1. Quien genera no valida.
2. La validación tiene que tocar la realidad: un dato, un documento original, una persona.
3. Se deja constancia de quién validó y cómo.

La IA que se evalúa a sí misma no está verificada. Está satisfecha.

#IACientífica #AgentesIA #GobernanzaIA

---

## Mar 1 dic · Interpretabilidad

Ya se puede mirar dentro de la IA. Lo que no existe es un estándar para auditarla.

Durante años nos dijeron que los modelos eran una caja negra. La interpretabilidad mecanicista, que estudia qué ocurre dentro del modelo cuando responde, ha avanzado tanto que MIT Technology Review la incluyó entre sus tecnologías destacadas de 2026 [VERIFICAR].

Pero hay un matiz que casi nadie cuenta: la propia comunidad investigadora reconoce que todavía no tiene un sistema estándar para auditar esos experimentos [VERIFICAR artículo].

Es decir, podemos mirar dentro, pero no hay un protocolo común para que lo que uno ve lo pueda comprobar otro.

Para una empresa, la consecuencia es práctica: cuando un proveedor diga que su modelo es "explicable", pregunta:
- ¿Explicable con qué método?
- ¿Revisado por quién?
- ¿Reproducible por un tercero?

Explicar no es auditar.

#Interpretabilidad #IAResponsable #GobernanzaIA #Auditoría

---

## Mié 2 dic · Fecha del AI Act

Hoy vence un plazo del AI Act del que casi nadie habla.

Desde hoy, los sistemas de IA generativa que ya estaban en el mercado antes de agosto tienen que cumplir la obligación de marcar sus contenidos de forma que se puedan detectar como generados por IA [VERIFICAR alcance del art. 50.2 y fecha en el Reglamento 2026/1744].

Y desde hoy también se aplica una nueva prohibición: los sistemas que generan material íntimo no consentido o de abuso sexual infantil [VERIFICAR].

¿Afecta a tu empresa si solo usa la IA, no la fabrica? La obligación de marcado recae sobre todo en quien la ofrece. Pero quien la usa para publicar tiene su propia pregunta: ¿sabemos qué contenidos hemos hecho con IA y cómo se identifican?

Si la respuesta es no, el jueves dejo una checklist.

#AIAct #IAGenerativa #Transparencia #GobernanzaIA

---

## Jue 3 dic · Plantilla de transparencia

Checklist de transparencia para contenidos hechos con IA

1. Inventario: qué tipos de contenido generamos con IA (texto, imagen, audio, vídeo).
2. Herramienta: cuál usamos y si marca el contenido de forma automática.
3. Conservación: si el marcado sobrevive a nuestra edición y publicación (redimensionar, exportar o subir a redes puede borrarlo).
4. Etiqueta visible: cuándo lo decimos al público y con qué fórmula.
5. Revisión humana: quién valida antes de publicar.
6. Registro: dónde queda constancia de qué se hizo con IA.
7. Responsable: nombre y cargo.

El punto 3 es el que más falla: el marcado existe, pero se pierde por el camino.

#Transparencia #AIAct #IAResponsable
