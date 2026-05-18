Actúa como un Experto en Data Science y Desarrollador Python Senior. Tu tarea es analizar la imagen adjunta (que contiene un gráfico/histograma técnico de investigación) y proporcionarme el código exacto de una celda para mi cuaderno de Google Colab que cumpla estrictamente con los siguientes requerimientos:

1. RECREACIÓN CON MATPLOTLIB Y NUMPY:
   - El código debe generar un gráfico de alta fidelidad idéntico al de la imagen, utilizando matplotlib y numpy para procesar o simular los datos numéricos necesarios.
   - Aplica estilos profesionales: tamaño de fuentes, etiquetas de ejes (X/Y), leyendas, colores académicos y configuraciones de rejilla (grid) idénticas a la figura original.

2. GENERACIÓN DE CÓDIGO TIKZ:
   - Dentro de la misma celda, define una función o bloque de código que traduzca o replique de forma vectorial fiel este mismo diseño utilizando código nativo PGF/TikZ (adecuado para compilación en LaTeX).
   - El código TikZ generado debe ser limpio, modular y autónomo (dentro de un entorno \begin{tikzpicture} ... \end{tikzpicture}).

3. INTERFAZ DE USUARIO E INYECCIÓN EN DISCO (IPYWIDGETS):
   - La celda de Colab debe renderizar una interfaz interactiva utilizando 'ipywidgets' que contenga:
     a) Un campo de texto (widgets.Text) para que yo ingrese el nombre del archivo (ej. 'histograma_error_orbital').
     b) Un botón de guardado (widgets.Button).
     c) Un componente de salida o etiqueta para mostrar el estado del proceso.
   - Al hacer clic en el botón, el script de Python debe:
     * Verificar si existe el directorio "workflow/workflow/outputs/codes/". Si no existe, debe crearlo automáticamente usando os.makedirs().
     * Asegurar que el nombre del archivo termine en '.tex'.
     * Escribir y almacenar el código TikZ generado directamente en un archivo de texto plano en dicha ruta.
     * Mostrar un mensaje claro en la interfaz que confirme el éxito del guardado o el error en caso de fallo.

Entrega únicamente el bloque de código limpio y listo para ejecutar en la celda de Colab, estructurado de forma elegante y con comentarios técnicos breves.