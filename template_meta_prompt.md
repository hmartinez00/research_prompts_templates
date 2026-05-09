Actúa como Editor Jefe de IEEE con amplia experiencia en la redacción de artículos académicos. 

Para el tema de investigación **{{contenido_insertado}}**, genera un **Desglose Temático Detallado** siguiendo estrictamente este esquema de tres partes:

**PARTE 1: ESTRUCTURA JSON**

Entrega un único bloque de código JSON con la siguiente estructura:

```json
{
  "titulo": "Título técnico en español",
  "folder_name": "Identificador alfanumérico del proyecto bajo la convención snake_case. Sin espacios en blanco. Usar '_' como separador",
  "abstract_preliminar": "Resumen técnico de 150 palabras siguiendo normas IEEE",
  "secciones": [
    {
      "nro": 1,
      "titulo_seccion": "Introducción",
      "objetivos": ["objetivo 1", "objetivo 2"],
      "subsecciones": ["1.1...", "1.2..."],
      "insumos": ["Tabla 1", "Eq. 1"],
      "llaves_bibtex": ["Key1", "Key2"]
    },
    // ... resto de secciones técnicas ...
    {
      "nro": N,
      "titulo_seccion": "Conclusiones",
      "objetivos": ["..."],
      "subsecciones": ["..."],
      "insumos": [],
      "llaves_bibtex": ["KeyX"]
    }
  ]
}
```

**RESTRICCIONES ESTRUCTURALES OBLIGATORIAS:**

- La **primera sección** (nro: 1) **debe ser siempre** "Introducción".
- La **última sección** **debe ser siempre** "Conclusiones" (o "Conclusiones y Trabajos Futuros" si es más apropiado).
- Entre la Introducción y las Conclusiones debes incluir las secciones técnicas principales relevantes al tema (entre 4 y 8 secciones en total).
- Estructura típica recomendada (ajusta según el tema): Introducción → Antecedentes / Estado del Arte → Metodología / Propuesta → Resultados / Análisis → Discusión → Conclusiones.

**PARTE 2: BLOQUES BIBLIOGRÁFICOS SECCIONALES**

Para cada sección, entrega un bloque de código independiente con las entradas en formato BibTeX.

**REQUISITOS OBLIGATORIOS PARA CADA REFERENCIA:**

- Fuentes **reales y verificables** (publicadas preferentemente entre 2022 y 2026).
- **Debe incluir siempre** el campo `url = {https://...}` con la **URL completa y accesible públicamente** (preferiblemente el enlace directo al artículo, PDF o página del editor).
- Si la referencia tiene DOI, **inclúyelo obligatoriamente** en el campo `doi = {10.xxxx/...}`.
- La suma total de referencias en TODAS las secciones debe ser ≤ 30.
- Formato limpio, listo para copiar/pegar directamente en `references.bib`.
- Usa el estilo BibTeX estándar compatible con IEEEtran.

**Ejemplo de entrada correcta:**
```bibtex
@article{key_ejemplo2025,
  author    = {Apellido, N. and Apellido2, I.},
  title     = {Título completo del artículo},
  journal   = {IEEE Transactions on ...},
  volume    = {XX},
  number    = {X},
  pages     = {XX--XX},
  year      = {2025},
  doi       = {10.1109/TXXX.2025.1234567},
  url       = {https://doi.org/10.1109/TXXX.2025.1234567},
  note      = {[Online]. Available: https://ieeexplore.ieee.org/document/1234567}
}
```

**PARTE 3: MAPA DE USO DE REFERENCIAS (POR SECCIÓN)**

Para cada sección, genera un bloque JSON independiente que funcione como diccionario asociativo, conectando cada `llave_bibtex` con su justificación y y directrices de integración:
```json
{
  "seccion_nro": 1,
  "titulo_seccion": "Nombre exacto de la sección",
  "mapa_uso": {
    "Key1": {
      "razon_seleccion": "Justificación técnica o metodológica de la elección (máx. 1 oración).",
      "guia_redaccion": "Instrucción precisa sobre cómo integrarla (ej: 'Usar en 1.1 para contrastar X vs Y, citando resultados de eficiencia y destacando limitaciones en entornos reales').",
      "subseccion_destino": "1.1"
    },
    "Key2": { "..." : "..." }
  }
}
```

**🔒 INSTRUCCIONES CRÍTICAS:**

1. **Coherencia absoluta**: Las claves en `llaves_bibtex` (PARTE 1), en los bloques `.bib` (PARTE 2) y en `mapa_uso` (PARTE 3) deben coincidir carácter por carácter.
2. La sección "Introducción" debe contener referencias de contexto y motivación.
3. La sección "Conclusiones" debe contener referencias para comparar resultados, discutir limitaciones y trabajos futuros.
4. **Sin redacción**: No generes texto narrativo, solo los bloques de código solicitados.
5. **Formato estricto**: Cada parte debe ir en su propio bloque de código. Nada de texto explicativo entre bloques.
6. **Enfoque IEEE**: Prioriza journals y conferencias indexadas, métricas cuantitativas y metodologías reproducibles.