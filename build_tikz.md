Actúa como un experto en visualización científica con LaTeX y TikZ.

A continuación recibirás código Python (Matplotlib/NumPy/Seaborn) que 
reproduce un gráfico. Tu tarea es traducirlo a código TikZ/pgfplots 
con la misma fidelidad estructural.

---

### CONTEXTO DE COMPILACIÓN

El código que generes será incluido vía `\input{}` en un `main.tex` 
con este preámbulo ya presente (no lo repitas):

\usepackage{tikz}
\usepackage{pgfplots}
\usepgfplotslibrary{groupplots}
\pgfplotsset{compat=1.18}
\usetikzlibrary{
    arrows.meta,
    positioning,
    calc,
    shapes.geometric,
    decorations.pathreplacing
}

---

### CÓDIGO PYTHON DE REFERENCIA

[PEGA AQUÍ EL CÓDIGO GENERADO POR EL PROMPT 1]

---

### PASO 1 — ANÁLISIS DE TRADUCCIÓN (responde antes de generar código)

Antes de escribir TikZ, declara explícitamente:

1. **Qué elementos se traducen con pgfplots** (ejes con datos numéricos, 
   curvas, puntos, barras)
2. **Qué elementos se traducen con TikZ puro** (anotaciones, flechas, 
   etiquetas flotantes, formas geométricas)
3. **Conversiones necesarias:** cómo mapeas los valores Python 
   (figsize, colores hex, fontsizes) a sus equivalentes LaTeX
4. **Limitaciones:** qué elementos de Matplotlib no tienen equivalente 
   directo en TikZ/pgfplots y cómo los aproximarás

---

### PASO 2 — GENERACIÓN DEL CÓDIGO TIKZ

Reglas estrictas de estructura:

1. Entrega ÚNICAMENTE el contenido dentro de 
   `\begin{tikzpicture} ... \end{tikzpicture}`
   Sin `\documentclass`, preámbulo ni `\begin{document}`

2. Organización interna obligatoria:
   % === PARÁMETROS ===
   % Define estilos y constantes al inicio con \tikzset{} o pgfkeys
   % Ningún valor hardcodeado dentro de los comandos de dibujo

   % === DATOS (si aplica) ===
   % Coordenadas o tablas con \addplot coordinates{} o \addplot table{}

   % === ESTRUCTURA PRINCIPAL ===
   % El entorno axis o los nodos tikz principales

   % === ANOTACIONES ===
   % Flechas, etiquetas, líneas de referencia sobre la figura

3. Criterio de herramienta:
   - Datos numéricos con ejes → `\begin{axis}...\end{axis}` (pgfplots)
   - Elementos esquemáticos puros → TikZ directo
   - Ambos presentes → pgfplots para datos, TikZ encima para anotaciones

4. Correspondencia con el código Python:
   - Cada variable del bloque PARÁMETROS del código Python debe tener 
     su equivalente declarado en el bloque % === PARÁMETROS === de TikZ
   - Los comentarios `# ASUNCIÓN:` del código Python deben mantenerse 
     como `% ASUNCIÓN:` en el TikZ

---

### CRITERIOS DE FIDELIDAD

Prioriza en este orden:
1. Estructura matemática (misma función, mismos datos)
2. Proporciones de ejes y escala
3. Relaciones visuales entre elementos
4. Equivalencia de estilo (usa xcolor para colores hex, 
   escala de grosores line width proporcional al original)

---

### RESTRICCIONES

- Código compilable con pdflatex sin paquetes adicionales al preámbulo dado
- Sin texto explicativo fuera del bloque de código
- Comentarios técnicos breves por sección, no por línea