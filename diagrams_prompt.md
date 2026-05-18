Actúa como un Ingeniero de Software Senior y Experto en Arquitectura de Sistemas. Tu tarea es analizar detalladamente la imagen PNG adjunta, la cual representa un diagrama técnico de una investigación en ingeniería de comunicaciones y control, y traducirla fielmente a código estructurado de Mermaid.js.

Para garantizar que el diagrama sea modular, estéticamente profesional y compatible con la importación nativa en plataformas como Draw.io, debes seguir estrictamente estas reglas de diseño:

1. COMPATIBILIDAD DE SINTAXIS (CRÍTICO): 
   - Utiliza únicamente conectores de flecha estándar (como "-->", "---" o "<-->").
   - Prohibido el uso de flechas de doble línea gruesa (como "==>") o cualquier codificación que pueda convertirse en entidades HTML (como "&gt;"), ya que rompen el motor de renderizado de Draw.io.
   - Si un enlace es bidireccional, represéntalo explícitamente usando "<-->".

2. ESTRUCTURA Y JERARQUÍA (Top-Down):
   - Inicia el diagrama con la dirección vertical usando "graph TB" (Top to Bottom).
   - Utiliza bloques "subgraph" para delimitar claramente las diferentes capas lógicas, niveles de software o entornos físicos que se aprecian en la imagen, manteniendo los nombres y títulos técnicos exactos.

3. ESTILIZACIÓN MINIMALISTA (Estilo Paper IEEE):
   - Define clases de estilo personalizadas (classDef) al inicio del código utilizando una paleta de colores limpia y académica (preferiblemente fondos blancos "#ffffff", bordes negros "#000000" o azul cobalto "#0047AB" para componentes críticos, y texto oscuro).
   - Evita el uso de fuentes de colores brillantes o estilos sobrecargados. No incluyas emojis dentro de los nombres de los nodos para evitar problemas léxicos.

4. FIDELIDAD TEXTUAL:
   - Conserva de manera exacta los términos técnicos, acrónimos y variables del diagrama original (por ejemplo: MAPE-K, SCP, Transformers, gNB, etc.). Si un nodo requiere saltos de línea para ajustarse al diseño original, utiliza la etiqueta "<br>".

Genera únicamente el bloque de código Mermaid.js dentro de un contenedor de código limpio, sin introducciones ni explicaciones adicionales, listo para ser copiado e inyectado directamente en el editor avanzado de Draw.io.