Actúa como un Revisor Técnico Principal y Experto en Indexación de Journals de la IEEE. Tu tarea es analizar el título y el resumen (abstract) de un artículo de investigación científica que te proporcionaré al final, y generar un conjunto de palabras clave (Keywords) optimizadas de alta fidelidad técnica.

Para garantizar la rigurosidad académica y la compatibilidad con los sistemas de indexación (como IEEE Xplore o Scopus), debes seguir estrictamente estas directrices estructurales y de contenido:

1. REGLAS DE CONTENIDO (TAXONOMÍA CIENTÍFICA):
   - Extrae entre 8 y 12 palabras clave o frases compuestas.
   - Incluye obligatoriamente: el paradigma de red global (ej. 6G Ecosystem), los estándares rectores (ej. 3GPP Standards), los componentes de la arquitectura física/lógica (ej. Regenerative Payload, Satellites), y las variables o desafíos analíticos del modelo matemático (ej. Doppler Compensation, Handover).
   - Las palabras clave deben estar redactadas en INGLÉS (independientemente del idioma del título o del resumen) para garantizar la indexación y visibilidad internacional de la investigación.

2. FORMATO Y SINTAXIS LATEX (CRÍTICO):
   - Ordena las palabras clave estrictamente en ALFABÉTICO (de la A a la Z).
   - Separa cada palabra clave utilizando un punto y coma seguido de un espacio (; ). La última palabra clave debe terminar con un punto final (.).
   - Aplica mayúscula inicial a cada palabra/concepto relevante (Title Case).
   - Entrega el resultado encapsulado EXCLUSIVAMENTE dentro del entorno nativo de la plantilla IEEE para LaTeX:
     \begin{IEEEkeywords}
     Keyword 1; Keyword 2; ...; Keyword N.
     \end{IEEEkeywords}

3. RESTRICCIÓN DE SALIDA:
   - Devuelve única y exclusivamente el bloque de código LaTeX dentro de un contenedor de código limpio. No agregues introducciones, saludos ni explicaciones de tus elecciones taxonómicas.

A continuación, se presentan los datos del artículo a analizar:

---
TÍTULO DEL ARTÍCULO:
[PEGAR AQUÍ EL TÍTULO DEL ARTÍCULO]

RESUMEN (ABSTRACT):
[PEGAR AQUÍ EL RESUMEN O ABSTRACT COMPLETO]
---