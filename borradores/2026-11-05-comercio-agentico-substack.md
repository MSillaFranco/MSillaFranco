# Borrador Substack (no publicado)

## Título
Tu agente compra, ¿quién firma? La gobernanza del comercio agéntico la están escribiendo los protocolos

## Subtítulo
Las redes de pago ya saben demostrar qué autorizaste. La ley todavía no sabe quién paga cuando el agente se equivoca.

---

### Qué es el comercio agéntico

El comercio agéntico es la compra que inicia y completa un agente de IA en nombre de una persona o una empresa: busca, compara, llena el carrito y paga, dentro de unos límites que alguien le ha dado.

No es ciencia ficción. Desde septiembre de 2025, los usuarios de ChatGPT en Estados Unidos pueden comprar sin salir del chat gracias al Agentic Commerce Protocol (ACP), un estándar abierto que han desarrollado Stripe y OpenAI.

### La industria ha construido la prueba antes que la norma

En poco más de un año, los grandes actores de pagos han presentado su propia pieza:

| Quién | Qué | Para qué sirve |
|---|---|---|
| Google | AP2 (Agent Payments Protocol) | Autorizar pagos iniciados por agentes mediante "mandatos" firmados |
| Stripe y OpenAI | ACP (Agentic Commerce Protocol) | Que un agente complete la compra con el comercio |
| Mastercard | Agent Pay | Que solo operen agentes registrados, con tokens trazables |
| Visa | Intelligent Commerce Connect (piloto) | Que los comercios acepten compras de agentes con distintos protocolos |
| EMVCo | Borrador de marco para pagos agénticos (septiembre de 2026) | Registrar la "intención autorizada" del consumidor durante toda la transacción |

La idea común es el mandato: un documento firmado que dice qué puede hacer el agente. En la versión vigente de AP2 hay dos tipos. El mandato de compra recoge lo pactado con el comercio. El mandato de pago autoriza el cargo en un medio de pago concreto. Además, un mandato puede ser "abierto" (el usuario firma los límites: hasta este importe, estas fechas, este tipo de producto) o "cerrado" (una sola compra concreta).

Dicho sin tecnicismos: la prueba de lo que autorizaste deja de ser tu palabra y pasa a ser un documento técnico firmado.

### Lo que falta: quién responde

El Fondo Monetario Internacional lo resume en una nota de abril de 2026: falta claridad regulatoria sobre la responsabilidad de los agentes en los pagos. Las reglas actuales presuponen intención humana, y el FMI apunta que también podría entrar en juego la responsabilidad por producto defectuoso cuando un agente causa daños después de desplegarse.

Un artículo académico publicado en el European Journal of Risk Regulation plantea la pregunta de fondo: ¿responde quien crea el agente, quien lo usa o la plataforma que procesa el pago?

### Y en Europa

La UE está terminando la reforma de sus normas de pagos (la directiva PSD3 y el Reglamento de Servicios de Pago). El acuerdo político llegó en noviembre de 2025 y el Consejo adoptó su posición el 29 de octubre de 2026. Falta el paso final del Parlamento y la publicación.

El texto refuerza la protección frente al fraude y reparte la responsabilidad según la autenticación y los controles de cada proveedor. Lo que no he encontrado es una regla específica para la compra que inicia un agente. Si existe, la buscaré en el texto definitivo.

### El marco de gobernanza

| Pregunta | Hoy |
|---|---|
| ¿Quién actúa? | El agente, con límites firmados por una persona o una empresa |
| ¿Quién responde? | Sin regla clara. Candidatos: quien crea el agente, quien lo usa, el comercio, el proveedor de pagos |
| ¿Qué norma aplica? | Normas de pagos pensadas para personas, contratos privados y las reglas de cada red |

Cuando la ley no decide, deciden los contratos y las reglas de las redes de pago. Esa es la parte que menos se está contando.

### Plantilla: política mínima de compras para agentes

1. **Alcance:** qué puede comprar el agente y qué no.
2. **Límites firmados:** importe por operación y por periodo, proveedores autorizados, plazos.
3. **Firmante:** persona responsable con nombre y cargo, no "el equipo".
4. **Confirmación humana:** a partir de qué importe o en qué casos.
5. **Registro:** qué se guarda de cada orden (mandato, carrito, pago) y quién lo revisa.
6. **Incidentes:** cómo se bloquea el agente, cómo se reclama y a quién se avisa.
7. **Contrato:** qué dicen las condiciones del proveedor del agente y del proveedor de pagos sobre errores.

### Preguntas frecuentes

**¿Puede ya un agente de IA pagar por mí?**
Sí, en entornos concretos. ChatGPT permite compras dentro del chat en EE. UU. y las redes de tarjetas tienen programas en marcha o en piloto.

**¿Quién paga si el agente compra mal?**
No hay una respuesta legal clara todavía. El FMI lo señala como un vacío. Hoy dependerá sobre todo de los contratos y de las reglas de cada red de pago.

**¿Qué puede hacer una empresa hoy?**
No esperar a la ley: fijar límites firmados, conservar el registro de cada orden y leer las condiciones de sus proveedores.

### La idea de fondo

El comercio agéntico no fallará por la tecnología: los protocolos ya saben demostrar qué se autorizó. Fallará donde siempre: en que nadie haya decidido quién firma, quién revisa y quién responde.

### Fuentes
- Google Cloud, anuncio de AP2: https://cloud.google.com/blog/products/ai-machine-learning/announcing-agents-to-payments-ap2-protocol
- Especificación AP2: https://ap2-protocol.org/ap2/specification/
- Stripe, documentación ACP: https://docs.stripe.com/agentic-commerce/protocols/acp
- OpenAI, Buy it in ChatGPT: https://openai.com/index/buy-it-in-chatgpt/
- Mastercard Agent Pay: https://www.mastercard.com/global/en/business/artificial-intelligence/mastercard-agent-pay.html
- Visa, nota de prensa: https://investor.visa.com/news/news-details/2026/Visa-Opens-the-Door-to-AI-Driven-Shopping-for-Businesses-Worldwide/default.aspx
- EMVCo, borrador: https://www.emvco.com/resources/emv-agentic-payments-framework-for-specifications-v1-0-draft-comment-period-ends-30-sept-2026/
- FMI, Note 2026/004: https://www.imf.org/en/publications/imf-notes/issues/2026/04/22/how-agentic-ai-will-reshape-payments-575560
- European Journal of Risk Regulation: https://www.cambridge.org/core/journals/european-journal-of-risk-regulation/article/ai-agents-in-payments-applications-risks-and-regulations/C2EF22C4CD9513A9A6459D10680A5D12
- Parlamento Europeo, acuerdo PSD3/PSR: https://www.europarl.europa.eu/news/en/press-room/20251121IPR31540/payment-services-deal-more-protection-from-online-fraud-and-hidden-fees
- Consejo de la UE, posición en primera lectura: https://data.consilium.europa.eu/doc/document/ST-8543-2026-ADD-1-REV-1/en/pdf

---
Nota interna (borrar antes de publicar): todo se ha contrastado sobre extractos de las fuentes primarias. Antes de publicar, abrir y releer la nota del FMI, la especificación de AP2 (nombres de los mandatos) y el estado de PSD3/PSR en EUR-Lex.
