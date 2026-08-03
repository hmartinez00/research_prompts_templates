Actúa como Diseñador Instruccional y Arquitecto de Presentaciones especializado en Reveal.js, con experiencia construyendo material didáctico técnico a partir de fuentes primarias (papers, notebooks, documentación, código, resultados experimentales).

Para el contenido fuente adjunto — PDF | Jupyter Notebook | Markdown | Artículo científico | Documentación técnica | Código fuente | Resultados experimentales), genera un **Plan de Presentación** siguiendo estrictamente este esquema de tres partes.

---

**PARTE 1: ESTRUCTURA JSON (`presentation_plan.json`)**

Entrega un único bloque de código JSON con la siguiente estructura:

```json
{
  "titulo": "Título de la presentación",
  "folder_name": "identificador_snake_case_sin_espacios",
  "tema_institucional": null,
  "idioma": "es",
  "resumen_general": "Resumen de 2-3 líneas del propósito pedagógico de la presentación completa",
  "sesiones": [
    {
      "nro": 1,
      "titulo_sesion": "Nombre de la sesión (usado como data-title de la sección padre)",
      "objetivos": ["objetivo pedagógico 1", "objetivo pedagógico 2"],
      "laminas": [
        {
          "id": "kebab-case-id-unico",
          "data_title": "Texto exacto para data-title (sidebar + título persistente)",
          "tipo": "portada | contenido | interactiva | cierre",
          "objetivo_pedagogico": "Qué debe entender/lograr el espectador con esta lámina específica",
          "insumos": [
            "Tabla 1 del documento fuente",
            "Fig. 3: diagrama de arquitectura",
            "Ecuación de descenso de gradiente (sección 4.2)",
            "Código: train.py, líneas 40-65",
            "Resultado experimental: precisión 94.2% (tabla 5)"
          ],
          "continuidad_visual": {
            "auto_animate_con": "id de la lámina previa que comparte un elemento, o null",
            "elemento_compartido": "Descripción breve de qué elemento 'vuela' entre ambas láminas (ej. una fórmula, un diagrama, una matriz)"
          },
          "animacion_sugerida": "fragment | reveal-anim | ninguna",
          "notas_narracion": "Guion breve opcional — insumo reutilizable para una futura timeline_sesionN.json de narración sincronizada"
        }
      ]
    }
  ]
}
```

**RESTRICCIONES ESTRUCTURALES OBLIGATORIAS:**

- La **primera lámina de la primera sesión** debe ser `"tipo": "portada"`, mapeada a la vista `global.portada` ya existente en el módulo.
- La **última lámina de la última sesión** debe ser `"tipo": "cierre"`, mapeada a la vista `global.preguntas` ya existente en el módulo.
- Cada `id` de lámina debe ser **único en toda la presentación** (no solo dentro de la sesión) — se usa tal cual como atributo `id` del `<x-slide>` para enlaces internos (`href="#/id"`) y como referencia para `data-auto-animate`.
- Cada entrada de `insumos` debe mapear 1:1 con un elemento **real e identificable** dentro del documento fuente (no inventar tablas, figuras o resultados que no estén presentes).
- `continuidad_visual.auto_animate_con` solo debe usarse entre láminas **contiguas** dentro de la misma sesión (restricción técnica de Auto-Animate en Reveal.js: solo interpola entre la lámina actual y la inmediatamente siguiente).
- Entre 4 y 10 láminas por sesión; entre 2 y 6 sesiones por presentación, ajustado a la extensión real del documento fuente.

---

**PARTE 2: REGISTRO INICIAL DE CLASES CSS (`class_registry.json`)**

Antes de escribir ninguna lámina, planifica el vocabulario visual completo que se necesitará a lo largo de toda la presentación. Esto es obligatorio porque el módulo **prohíbe CSS inline dentro de las láminas** — todo estilo debe expresarse mediante clases predefinidas y comentadas.

```json
{
  "clases": [
    {
      "nombre": "slide-two-column",
      "proposito": "Layout de dos columnas: contenido a la izquierda, imagen/diagrama a la derecha",
      "propiedades_clave": ["display: flex", "gap: 40px", "align-items: center"],
      "implementada": false,
      "sesiones_que_la_usan": [1, 2]
    }
  ]
}
```

**Reglas:**
- Nombres semánticos, kebab-case, sin prefijo `slide-` en el JSON (el prefijo se agrega automáticamente al escribir el CSS real, ver segundo prompt).
- Cada clase debe ser **reutilizable por múltiples láminas** — evita planificar una clase de un solo uso salvo que sea genuinamente necesario (ej. un layout muy específico de una lámina interactiva única).
- Piensa en términos de patrones de layout recurrentes: portada, dos columnas, cuadrícula de tarjetas, comparación lado a lado, línea de tiempo, matriz/grid interactivo, cita destacada, bloque de código.
- **`implementada` siempre debe ser `false` en este documento.** Este campo distingue una clase *planificada* (solo existe como intención, sin CSS real todavía) de una clase *materializada* (ya tiene reglas CSS escritas en `styles.blade.php`). En este plan inicial ninguna clase tiene CSS real todavía — el segundo prompt (constructor de sesiones) es quien la marca como `true` la primera vez que efectivamente escribe su CSS.

---

**PARTE 3: REGISTRO INICIAL DE COMPORTAMIENTOS JS (`js_registry.json`)**

Planifica también qué interactividad JavaScript necesitará la presentación, sin escribir el código todavía.

```json
{
  "comportamientos": [
    {
      "nombre": "matrixConvolutionSimulator",
      "proposito": "Anima el recorrido de un kernel sobre una matriz de entrada, revelando progresivamente el mapa de salida",
      "implementada": false,
      "sesiones_que_lo_usan": [2]
    }
  ]
}
```

**Reglas:**
- Solo planifica comportamientos que vayan **más allá** de lo que Reveal.js ya provee nativamente (fragments, Auto-Animate, transiciones). No planifiques "mostrar texto al avanzar" — eso ya lo resuelve `class="fragment"`.
- Cada comportamiento debe tener un nombre de función único en camelCase, que se usará literalmente como nombre de función JavaScript en el segundo prompt.
- **`implementada` siempre debe ser `false` en este documento**, por el mismo motivo que en `class_registry.json`: aquí solo se planifica qué comportamiento existirá, no se escribe su código todavía.

---

**🔒 INSTRUCCIONES CRÍTICAS:**

1. Este plan es la **única fuente de verdad** que consultará el segundo prompt (constructor de sesiones) — debe ser autocontenido y no requerir volver a leer el documento fuente completo.
2. **Sin redacción de código real**: no generes Blade, CSS ni JS en este documento — solo planificación estructurada.
3. Verifica que la suma de todos los `id` de lámina en `sesiones[].laminas[].id` sea única antes de entregar la respuesta.
4. Coherencia absoluta: cualquier nombre de clase referenciado implícitamente por el `tipo` o `objetivo_pedagogico` de una lámina debe existir en `class_registry.json`, y cualquier comportamiento sugerido por `animacion_sugerida` (si no es `fragment`/`reveal-anim`/`ninguna`) debe existir en `js_registry.json`. Todas las entradas de ambos registros deben llevar `"implementada": false` en este documento — es el segundo prompt quien las materializa.
5. Usa las vistas ya existentes del módulo (`global.portada`, `global.preguntas`) para las láminas de apertura y cierre — no inventes nombres alternativos para estas dos.

**Formato de salida**: exactamente tres bloques de código (```json para cada parte), sin texto explicativo entre ellos.