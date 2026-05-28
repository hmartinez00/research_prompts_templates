Actúa como un experto en visualización científica con LaTeX/TikZ y Python. 
Tu tarea es analizar la imagen adjunta y generar una celda autocontenida 
para Google Colab.

---

### CONTEXTO DE COMPILACIÓN

El código TikZ que generes será incluido vía `\input{}` en un `main.tex` 
que ya contiene este preámbulo (no lo repitas):

\usepackage{tikz}
\usepackage{pgfplots}
\usepgfplotslibrary{groupplots}
\pgfplotsset{compat=1.18}
\usetikzlibrary{arrows.meta, positioning, calc, shapes.geometric, 
                decorations.pathreplacing}

---

### PASO 1 — ANÁLISIS DE LA IMAGEN

Antes de generar código, describe brevemente:
- Tipo de gráfico (dispersión, barras, función matemática, diagrama, etc.)
- Elementos presentes: ejes, etiquetas, anotaciones, leyendas, colores
- Si la imagen es ambigua o contiene múltiples gráficos, descríbelo 
  explícitamente y pregunta antes de continuar

---

### PASO 2 — RECREACIÓN EN MATPLOTLIB (validación visual)

Genera el código Matplotlib que replique la estructura del gráfico 
con estilo académico (sin grid decorativo, fuente serif si es posible, 
proporciones similares al original).

Criterio de fidelidad: captura la estructura y datos, no los píxeles exactos.

Si el gráfico es puramente esquemático o conceptual (sin datos numéricos), 
omite este paso e indícalo.

---

### PASO 3 — GENERACIÓN DEL CÓDIGO TIKZ

Reglas estrictas:
- Entrega ÚNICAMENTE el contenido dentro de 
  `\begin{tikzpicture} ... \end{tikzpicture}`
- Prohibido incluir `\documentclass`, preámbulo o `\begin{document}`
- Usa `\begin{axis}...\end{axis}` (pgfplots) para gráficos con datos 
  numéricos o ejes técnicos
- Usa TikZ puro para elementos esquemáticos, diagramas o decorativos
- Si el gráfico tiene ambas partes, combínalos: pgfplots para los datos, 
  TikZ para las anotaciones encima

---

### PASO 4 — INTERFAZ EN IPYWIDGETS

Genera una celda con estos tres bloques en orden:

**Bloque A — Visualización Matplotlib**
El código del Paso 2 (si aplica).

**Bloque B — String TikZ**
El código TikZ almacenado en una variable `tikz_code = """ ... """`.

**Bloque C — Widgets de exportación**
Incluye:

1. `widgets.Text` para nombre de archivo (valor por defecto: `"figura_01"`)

2. Botón "💾 Guardar en disco":
   - Ruta destino: `outputs/tikz/` (relativa al notebook, sin redundancias)
   - Crea el directorio con `Path(...).mkdir(parents=True, exist_ok=True)`
   - Confirma con `widgets.Label` el path completo donde se guardó

3. Botón "📋 Copiar al portapapeles":
   - Detecta el entorno primero:
     - Si `google.colab` está disponible → usa `IPython.display.Javascript` 
       con `navigator.clipboard.writeText()`
     - Si no (Jupyter local) → usa `pyperclip.copy()` con try/except 
       que muestre un mensaje claro si falla
   - Confirma la acción con `widgets.Label`

---

### RESTRICCIONES GLOBALES

- Sin imports innecesarios; declara todos los imports al inicio de la celda
- Todo el código debe ejecutarse sin errores en un entorno Colab limpio 
  (sin configuración previa)
- Añade comentarios técnicos breves en cada sección, no en cada línea
- No incluyas texto explicativo fuera del bloque de código

---

### EJEMPLO DE ESTRUCTURA ESPERADA (esqueleto)

```py
# === IMPORTS ===
import ...

# === A: VISUALIZACIÓN MATPLOTLIB ===
fig, ax = plt.subplots(...)
...
plt.show()

# === B: CÓDIGO TIKZ ===
tikz_code = r"""
  % contenido tikzpicture aquí
"""

# === C: INTERFAZ DE EXPORTACIÓN ===
nombre_archivo = widgets.Text(...)
btn_guardar    = widgets.Button(...)
btn_copiar     = widgets.Button(...)
output         = widgets.Output()

def on_guardar(b): ...
def on_copiar(b):  ...

btn_guardar.on_click(on_guardar)
btn_copiar.on_click(on_copiar)

display(nombre_archivo, btn_guardar, btn_copiar, output)

```
