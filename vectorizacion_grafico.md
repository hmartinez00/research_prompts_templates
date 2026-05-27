Actúa como un Experto en Data Science y Desarrollador Python Senior. Tu tarea es analizar la imagen adjunta y proporcionarme una celda para Google Colab que cumpla con:

### 1. CONVENCIÓN DE COMPILACIÓN (CONTEXTO MAESTRO)
Todo código TikZ generado será incluido mediante `\input{}` en un archivo `main.tex` que ya contiene:

```latex
% --- PREÁMBULO MAESTRO (MANTÉN ESTO EN TU MAIN.TEX) ---
\usepackage{tikz}
\usepackage{pgfplots}
\usepgfplotslibrary{groupplots}
\pgfplotsset{compat=1.18}

% Librerías necesarias para los dibujos modulares que vamos a generar
\usetikzlibrary{
    arrows.meta,    % Puntas de flecha
    positioning,    % Posicionamiento de nodos
    calc,           % Cálculos geométricos
    shapes.geometric,
    decorations.pathreplacing
}
% ------------------------------------------------------

```

### 2. REQUERIMIENTOS DE CÓDIGO
1. **RECREACIÓN ANALÍTICA (MATPLOTLIB):** Genera la visualización para validación inmediata en el cuaderno (estilo académico).
2. **GENERACIÓN TIKZ MODULAR:** - El código debe ser EXCLUSIVAMENTE el contenido dentro del entorno `\begin{tikzpicture} ... \end{tikzpicture}`.
   - Prohibido incluir preámbulos, `\documentclass` o `\begin{document}`.
   - Usa `pgfplots` (`\begin{axis} ... \end{axis}`) para cualquier trazado técnico o basado en datos.
3. **INTERFAZ INTERACTIVA (IPYWIDGETS):**
   - Renderiza un `widgets.Text` para el nombre del archivo.
   - Renderiza dos botones: 
     a) **Guardar en disco:** Crea directorio "workflow/workflow/outputs/codes/" y guarda el `.tex`.
     b) **Copiar al portapapeles:** Utiliza `pyperclip.copy()` o la función `IPython.display.Javascript` para copiar el código generado a la memoria del sistema.
   - Muestra un `widgets.Output` o `Label` para confirmar el éxito de ambas acciones.

### 3. FORMATO DE ENTREGA
Entrega únicamente el bloque de código limpio, profesional y con comentarios técnicos explicativos.

