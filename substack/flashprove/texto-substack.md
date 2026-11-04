# Pagas por un modelo. ¿Quién te asegura que es ese?

**Subtítulo:** Anthropic ha publicado un prototipo que demuestra con criptografía qué modelo ha generado una respuesta. Todavía es caro y limitado. Pero deja a la vista una pregunta que casi ningún contrato de IA contesta.

*Ochin Kraso · 4 de noviembre de 2026*

---

Cuando una empresa contrata un servicio de IA, recibe texto. No recibe pruebas.

El contrato dice «modelo X». Lo que responde al otro lado puede ser ese modelo, una versión recortada para que salga más barata o un modelo distinto con el mismo nombre comercial. No digo que ocurra. Digo que hoy, en la mayoría de los casos, el cliente no tiene forma de comprobarlo.

En publicidad aprendí pronto una regla sencilla: nadie paga una campaña sin justificante de emisión. El anunciante no se fía de la palabra del medio; pide la prueba de que el anuncio salió donde y cuando se pactó. Con la IA estamos pagando sin justificante.

## Qué ha pasado

El 2 de noviembre, el Frontier Red Team de Anthropic, junto con investigadores de EPFL, MIT, StarkWare y Succinct, publicó **FlashProve**, un prototipo de lo que llaman *inferencia demostrable*.

La idea, sin tecnicismos: el proveedor registra una «huella» del modelo que dice usar. Cada vez que responde, puede generar una prueba criptográfica de que esa respuesta salió exactamente de ese modelo. Quien recibe la prueba la comprueba sin necesidad de ver el modelo por dentro. Es lo que en criptografía se llama una prueba de conocimiento cero: demuestras algo sin enseñar el secreto.

Lo han probado con **Llama 4 Maverick**, un modelo abierto de Meta de unos 400.000 millones de parámetros, y han liberado el código con licencia Apache 2.0.

## Para qué sirve, según sus autores

Anthropic plantea cuatro usos:

- **Reguladores:** pedir al proveedor certificados de las respuestas servidas en un periodo y comprobar que solo se usaron modelos aprobados.
- **Clientes que compran a través de intermediarios:** confirmar que el servicio que revende o enruta modelos está sirviendo el que se ha pagado.
- **Evaluadores:** asegurarse de que el modelo que están evaluando es el mismo que luego se despliega.
- **Seguridad:** detectar respuestas manipuladas o modelos sustituidos.

El segundo punto es el que más debería interesar a cualquier responsable de compras o de sistemas. Cada vez más herramientas de oficina llevan dentro el modelo de otro, y la cadena de proveedores se alarga.

## La letra pequeña

Anthropic lo presenta como prototipo de investigación, y conviene tomárselo así:

- **Es caro.** Generar la prueba cuesta entre 70 y 95 veces más tiempo de GPU que obtener la respuesta normal.
- **Es corto.** Solo cubre conversaciones de hasta 1.024 tokens, unas pocas páginas de texto.
- **Es estricto.** Funciona cuando el modelo elige siempre la palabra más probable. Las respuestas habituales, que llevan algo de variación aleatoria, pueden apartarse de lo que se demuestra.
- **No lo esconde todo.** Protege los pesos del modelo, no su arquitectura.

Hoy no es una herramienta para el día a día. Es la demostración de que el problema tiene solución técnica.

## Quién actúa, quién responde, qué norma aplica

**Quién actúa.** Tres eslabones: el laboratorio que entrena el modelo, el proveedor o intermediario que lo empaqueta en un servicio y la empresa que lo contrata y lo pone delante de sus empleados y clientes.

**Quién responde.** Sobre el papel, el proveedor, según lo que diga el contrato. En la práctica, si el contrato no fija qué modelo y qué versión se usan, ni da derecho a comprobarlo, la responsabilidad se queda en una promesa.

**Qué norma aplica.** En la Unión Europea, el Reglamento de IA impone desde agosto de 2025 obligaciones de documentación y transparencia a los proveedores de modelos de propósito general. *Mi lectura, que conviene contrastar con el texto:* esas obligaciones no exigen demostrar, respuesta a respuesta, qué modelo ha contestado. Hoy esa garantía solo puede venir del contrato.

El dato de contexto que lo hace urgente: Mistral acaba de publicar en abierto Mistral Large 4. Con modelos abiertos de ese tamaño, cualquiera puede montar un servicio, ajustarlo o quitarle protecciones. Más opciones para el comprador, y más motivos para saber qué está comprando.

## Plantilla: cuatro cláusulas antes de firmar con un proveedor de IA

Cópialas y pásalas a tu departamento de compras o a tu asesoría jurídica. Son un punto de partida, no texto legal cerrado.

1. **Identificación.** «El proveedor identificará el modelo y la versión exactos que prestan el servicio contratado.»
2. **Cambios.** «Cualquier sustitución o actualización del modelo se comunicará con [30] días de antelación y por escrito.»
3. **Verificación.** «El cliente podrá solicitar evidencias de que el modelo en uso es el contratado, incluidas pruebas técnicas cuando estén disponibles.»
4. **Responsabilidad.** «Si el modelo en uso no coincide con el contratado, el proveedor responderá de [definir: penalización, resolución, indemnización].»

La cuarta es la que más cuesta negociar y la que más importa. Sin ella, las tres primeras son una declaración de buenas intenciones.

## Cierre

La IA en la oficina no falla por la tecnología, falla por la gobernanza. FlashProve demuestra que la verificación es posible. Que llegue a tu contrato depende de que alguien en tu organización la pida.

**¿Sabes qué modelo hay detrás de las herramientas de IA que usa tu equipo? ¿Y quién te lo garantiza?** Te leo en comentarios.

---

### Fuentes

- Anthropic, *Progress on provable inference for large language models* (2/11/2026): https://www.anthropic.com/research/provable-inference
- Mistral, Mistral Large 4 con pesos abiertos: https://mistral.ai/news/mistral-large-4-oss/
- Reglamento (UE) 2024/1689 de Inteligencia Artificial (EUR-Lex): https://eur-lex.europa.eu/eli/reg/2024/1689/oj
