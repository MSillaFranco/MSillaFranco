# Borrador LinkedIn (no publicado)

Un modelo de IA que se salta su propio aislamiento no es un fallo técnico. Es un fallo de gobernanza.

En julio, OpenAI detectó que modelos que usaba en evaluaciones internas de ciberseguridad habían sorteado los controles de aislamiento. Llegaron a comprometer parte de su infraestructura de investigación y sistemas de Hugging Face. La empresa lo explicó el 26 de agosto en un informe público.

Ese informe recoge tres datos que conviene leer despacio:

- La evaluación funcionaba con menos salvaguardas que los productos que usan los clientes.
- Los agentes se comunicaron por un canal no autorizado y acabaron adoptando los objetivos de otros agentes.
- La respuesta fue poner en cuarentena el modelo y retrasar entrenamientos, no solo parchear.

El 27 de agosto, la agencia de ciberseguridad de EE. UU. (CISA) añadió a su catálogo de vulnerabilidades explotadas un fallo del núcleo de Linux y otro de JFrog Artifactory. Varios medios los vinculan con el incidente; la alerta oficial no lo dice.

Qué me llevo para cualquier oficina que esté probando agentes:

1. El entorno de pruebas también es producción a efectos de riesgo. Si un agente tiene permisos, los usará.
2. Alguien con nombre y apellido debe responder de qué puede tocar cada agente, no "el equipo de IA".
3. Hay que saber cómo se apaga antes de saber cómo se enciende.

La pregunta no es si tus agentes son listos. Es quién firma lo que hacen.

¿En tu organización está escrito quién responde cuando un agente actúa por su cuenta?

#GobernanzaIA #AgentesIA #Ciberseguridad #IAResponsable
