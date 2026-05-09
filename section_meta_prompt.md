=== SPRINT DE ESCRITURA: SECCIÓN {{section_number}} ===

PAPER: {{project_title}}
SECCIÓN: {{sec_title}}

--- CONTEXTO Y OBJETIVOS ---
OBJETIVOS: {{objetivos}}
SUBSECCIONES REQUERIDAS: {{subsecciones}}
INSUMOS (Tablas/Ecuaciones/Figuras): {{insumos}}

--- CITAS BIBLIOGRÁFICAS OBLIGATORIAS ---
Claves BibTeX: {{llaves_bibtex}}

{{instrucciones_citacion}}

--- ⛔ RESTRICCIONES MODULARES (CRÍTICO) ---
Este fragmento se insertará vía \input{section_N.tex}. 
Prohibido cualquier comando de preámbulo, \documentclass, paquetes, configuración de bibliografía o metadatos.

--- ✅ INSTRUCCIONES DE HUMANIZACIÓN AVANZADA (OBLIGATORIO) ---

Escribe como un investigador senior con voz propia, no como un modelo de lenguaje. Tu texto debe transmitir experiencia acumulada, juicio crítico y fluidez académica real.

**Técnicas de humanización avanzada que DEBES aplicar:**

- **Burstiness fuerte**: Mezcla extrema de oraciones cortas y contundentes con oraciones largas y complejas. Varía el largo de párrafos (algunos de 2-3 líneas, otros más desarrollados).
- **Vocabulario y estructuras variables**: Evita repetición de conectores (por lo tanto, además, sin embargo). Usa alternativas naturales y sofisticadas.
- **Aperturas no genéricas**: Nunca empieces sección o subsección con "La...", "El...", "Este...", "Los...". 
  Ejemplos deseados:  
  - "Aunque los enfoques tradicionales han aportado..."  
  - "Uno de los desafíos persistentes que surge al analizar..."  
  - "Resulta revelador observar cómo..."  
  - "Lejos de ser un asunto resuelto, la literatura reciente sugiere..."  
  - "Particularmente llamativo es el hecho de que..."

- **Pensamiento crítico y matiz**: Incluye hedging natural ("parece sugerir", "tiende a", "en muchos casos estudiados", "no obstante, cabe matizar"), breves análisis críticos o señalamiento de limitaciones.
- **Flujo orgánico**: Crea transiciones que parezcan pensadas por un humano (referencias hacia atrás y hacia adelante leves, conexiones conceptuales inesperadas pero lógicas).
- **Toque de voz académica personal**: Escribe como si hubieras reflexionado profundamente sobre el tema, no como si estuvieras resumiendo información.
- **Pequeñas "imperfecciones controladas"**: Ligera asimetría en estructuras paralelas, uso ocasional de construcciones más coloquiales dentro de lo formal (sin abusar).

**Estilo general**: Académico riguroso pero legible, con profundidad intelectual y naturalidad. Evita perfección robótica.

--- ⚙️ FORMATO DE SALIDA ESTRICTO ---

Tu respuesta debe contener **exactamente dos bloques**:

**BLOQUE 1 – Contenido LaTeX**
```latex
\section{Título de la Sección}
\subsection{Subsección}
Texto con estilo humano avanzado aquí y citas \cite{Key} integradas orgánicamente...

\begin{figure}[h]
\centering
\includegraphics[width=\linewidth]{nombre.png}
\caption{Descripción clara y técnica}
\label{fig:nombre}
\end{figure}
```

**BLOQUE 2 – Prompts de Imagen**
```json
{
  "fig1.png": "2D technical vector diagram, engineering schematic, flat design, minimalista, fondo blanco puro, colores azul cobalto #0047AB y gris técnico #4A4A4A, sin sombras, sin gradientes, sin texto incrustado..."
}
```

**Reglas técnicas adicionales:**
1. Extensión aproximada: 650-900 palabras.
2. Usa solo las subsecciones solicitadas.
3. Integra las citas BibTeX de forma natural y orgánica dentro del argumento.
4. Figuras y tablas en formato IEEE estándar.
5. Estilo visual de las imágenes:
   - Estilo: 2D technical vector diagram, engineering schematic, flat design, minimalista
   - Fondo: blanco puro
   - Colores principales: Azul cobalto (#0047AB), gris técnico (#4A4A4A), negro
   - Sin sombras, sin gradientes, sin texto dentro de la imagen, sin elementos decorativos