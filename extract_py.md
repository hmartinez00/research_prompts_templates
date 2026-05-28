Actúa como un experto en visualización científica con Python.

Tu tarea es analizar la imagen adjunta y generar código Python que la 
reproduzca con la mayor fidelidad posible en Google Colab.

---

### PASO 1 — ANÁLISIS PREVIO (responde antes de generar código)

Describe con precisión:

1. **Tipo de gráfico:** (línea, dispersión, barras, histograma, heatmap, 
   función matemática, diagrama, etc.)
2. **Datos observados:** rangos de ejes, unidades, escala (lineal/log), 
   valores aproximados de puntos o curvas visibles
3. **Elementos estructurales:** título, etiquetas de ejes, leyenda, 
   anotaciones, líneas de referencia, grillas
4. **Estilo:** paleta de colores, grosor de líneas, marcadores, 
   transparencias, tipografía visible
5. **Ambigüedades:** si algo no es legible o interpretable con certeza, 
   indícalo explícitamente antes de asumir

No generes código hasta completar este análisis.

---

### PASO 2 — GENERACIÓN DEL CÓDIGO

Usando el análisis anterior, genera una celda Python única con esta 
estructura:

# === IMPORTS ===
# Solo los necesarios: matplotlib, numpy, seaborn según el caso

# === PARÁMETROS DEL GRÁFICO ===
# Todos los valores numéricos extraídos de la imagen declarados 
# como variables nombradas aquí arriba.
# Ningún número hardcodeado dentro del código de dibujo.
# Ejemplo:
#   x_min, x_max = 0, 10
#   color_linea_principal = "#2C7BB6"
#   grosor_linea = 2.0

# === DATOS ===
# Arrays numpy o estructuras de datos claramente nombradas

# === FIGURA ===
# Construcción del gráfico respetando:
# - Proporciones visuales de la imagen original (figsize)
# - Estilo académico: sin grid decorativo salvo que esté en el original,  
#   fondo blanco, tipografía legible
# - Cada elemento del gráfico en una línea separada con comentario breve

# === RENDER ===
plt.tight_layout()
plt.show()

---

### CRITERIOS DE FIDELIDAD

Prioriza en este orden:
1. Estructura matemática o lógica del gráfico (qué representa)
2. Proporciones y rangos de ejes
3. Relaciones visuales entre elementos (posición relativa, escala)
4. Estilo visual (colores, grosores, tipografía)

Si la imagen es ambigua en algún criterio, documéntalo como comentario 
en el código con el prefijo `# ASUNCIÓN:`.

---

### RESTRICCIONES

- Código ejecutable en Colab limpio sin configuración previa
- Sin texto explicativo fuera del bloque de código
- Sin imports no utilizados
- El bloque de parámetros debe ser suficiente para ajustar el gráfico 
  sin tocar el código de dibujo