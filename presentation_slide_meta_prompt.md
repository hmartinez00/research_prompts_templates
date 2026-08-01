=== SPRINT DE CONSTRUCCIÓN: SESIÓN {{session_number}} ===

PRESENTACIÓN: {{project_title}}
CARPETA: {{folder_name}}
SESIÓN: {{session_title}}

--- CONTEXTO Y OBJETIVOS (desde presentation_plan.json) ---
OBJETIVOS DE LA SESIÓN: {{objetivos}}
LÁMINAS A CONSTRUIR (bloque completo de `sesiones[nro={{session_number}}]` del plan): {{laminas_json}}

--- REGISTRO VIGENTE (evita duplicar — acumulado de sesiones anteriores) ---
CLASES CSS YA DEFINIDAS: {{class_registry_actual}}
COMPORTAMIENTOS JS YA DEFINIDOS: {{js_registry_actual}}

--- ⛔ RESTRICCIONES DEL MÓDULO (CRÍTICO — arquitectura Laravel 12 + Reveal.js) ---

1. **Cero CSS inline dentro de las láminas.** Ningún atributo `style="..."` en el HTML de una lámina. Todo estilo se expresa mediante clases ya existentes en el registro, o clases nuevas que declares en el BLOQUE 2, cada una con un comentario explicando su propósito antes de su definición.

2. **Cada lámina es un archivo Blade independiente**, ruta `sesion{{session_number}}/{id_lamina}.blade.php`. Nunca incluyas `<html>`, `<body>`, ni `<section>` — el componente `<x-slide>` del módulo ya provee el `<section>` contenedor. El archivo debe iniciar en `<div class="slide-container ...">`.

3. **Nomenclatura de clases**: todo nombre de clase de layout/estructura lleva el prefijo `slide-` (ej. `slide-two-column`, `slide-matrix-grid`). Evita nombres genéricos como `.box`, `.title`, `.card` sin prefijo — pueden colisionar con el tema institucional activo o con Reveal.js.

4. **`data-title` obligatorio** en cada entrada de `<x-slide>` del BLOQUE 4 (usado por el sidebar de navegación y el título persistente de la lámina).

5. **Continuidad visual entre láminas** (campo `continuidad_visual` del plan): si `auto_animate_con` no es `null`, el elemento compartido debe llevar el **mismo `data-id`** en ambas láminas (la actual y la referenciada), y ambos `<x-slide>` correspondientes en el BLOQUE 4 deben incluir `data-auto-animate="true" data-auto-animate-easing="ease-in-out"`.

6. **Animación de aparición progresiva dentro de una misma lámina**: si `animacion_sugerida` es `"fragment"`, usa `class="fragment fade-right"` (o la variante de dirección que corresponda: `fade-up`, `fade-left`, `fade-down`) sobre el elemento a revelar — es una capacidad nativa de Reveal.js, no reinventarla. Si es `"reveal-anim"`, usa exclusivamente el comportamiento ya registrado con ese nombre en `js_registry_actual` (no crear uno nuevo si ya existe).

7. **Imágenes y diagramas**: siempre vía la directiva `@externalAsset('sesion{{session_number}}.img.nombre.ext')`. Si el insumo depende explícitamente del tema institucional (branding, logo), usa `\App\Helpers\CustomHelper::external_asset('img.nombre.ext', null, 'nombre_tema')`. Nunca URLs absolutas de terceros ni rutas hardcodeadas de otro proyecto.

8. **Todo bloque JavaScript debe comentarse por función/bloque lógico**, explicando qué hace y cuándo se dispara — no comentarios línea por línea triviales, sino intención. Cualquier función que consulte o modifique el DOM debe:
   - Recibir el elemento de la lámina activa como parámetro (nunca usar `document.querySelectorAll(...)` sin acotar).
   - Conectarse al ciclo de vida real de Reveal (`Reveal.on('ready', ...)`, `Reveal.on('slidechanged', ...)`), nunca depender en solitario de `DOMContentLoaded` ni de temporizadores globales sin scope de lámina.
   - Limpiar cualquier `setInterval`/`setTimeout`/listener propio al salir de la lámina (evitar fugas de comportamiento entre láminas, dado que Reveal.js mantiene todas las secciones montadas simultáneamente en el DOM).

9. Prohibido cualquier `<script>` o `<style>` suelto dentro del archivo de una lámina individual. Todo CSS va al BLOQUE 2 (fragmento para `styles.blade.php`), todo JS va al BLOQUE 3 (fragmento para `scripts.blade.php`).

--- ⚠️ NOTA DE ARQUITECTURA: SCOPE DE JAVASCRIPT (LECCIÓN APRENDIDA DEL MÓDULO) ---

Reveal.js mantiene **todas** las láminas de la presentación montadas simultáneamente en el DOM, incluso las que no están visibles. Un `document.querySelectorAll('.mi-clase')` sin acotar a la lámina activa animará o afectará elementos de otras láminas fuera de pantalla, produciendo comportamiento errático (orden de animación incorrecto, retrasos acumulados, temporizadores duplicados). Todo comportamiento nuevo debe seguir este patrón:

```javascript
function miComportamiento(slideElement) {
    const elementos = slideElement.querySelectorAll('.mi-clase'); // acotado, no global
    // ...
}

Reveal.on('slidechanged', event => {
    if (event.currentSlide.querySelector('.mi-clase')) {
        miComportamiento(event.currentSlide);
    }
});
```

--- ⚙️ FORMATO DE SALIDA ESTRICTO ---

Tu respuesta debe contener **exactamente cinco bloques**, en este orden:

**BLOQUE 1 — Archivos Blade de Láminas**
```blade
{{-- sesion{{session_number}}/id_lamina.blade.php --}}
<div class="slide-container slide-two-column">
    <!-- contenido de la lámina, sin CSS inline -->
</div>
```
(uno por cada lámina listada en `laminas_json`, cada archivo claramente rotulado con su ruta en el comentario de apertura)

**BLOQUE 2 — Adición a `styles.blade.php` (solo clases NUEVAS de esta sesión)**
```css
/* ==========================================
   SESIÓN {{session_number}}: {{session_title}}
   ========================================== */

/* .slide-nombre-clase
   Qué layout/estilo resuelve, en una línea.
   Usado en: id-lamina-1, id-lamina-3 */
.slide-nombre-clase {
    /* ... */
}
```
Si ninguna clase nueva es necesaria (todo se resuelve con el registro vigente), indica explícitamente `/* Sin clases nuevas en esta sesión — reutiliza el registro vigente. */`.

**BLOQUE 3 — Adición a `scripts.blade.php` (solo comportamientos NUEVOS de esta sesión)**
```javascript
/**
 * nombreDelComportamiento
 * ---------------------------------------------------------
 * Qué hace: descripción funcional breve.
 * Cuándo corre: en qué lámina(s) se activa y bajo qué condición se detiene.
 */
function nombreDelComportamiento(slideElement) {
    // ...
}

Reveal.on('slidechanged', event => {
    if (event.currentSlide.querySelector('#selector-caracteristico')) {
        nombreDelComportamiento(event.currentSlide);
    }
});
```
Si ningún comportamiento nuevo es necesario, indica explícitamente `// Sin comportamientos nuevos en esta sesión.`

**BLOQUE 4 — Entradas para `manifest.blade.php`**
```blade
{{-- Pegar dentro de <section data-title="{{session_title}}" data-session="sesion{{session_number}}"> --}}
<x-slide view="sesion{{session_number}}.id_lamina" data-title="..." />
```

**BLOQUE 5 — Actualización de Registros (para la siguiente sesión)**
```json
{
  "nuevas_clases": [
    { "nombre": "slide-nombre-clase", "proposito": "..." }
  ],
  "nuevos_comportamientos": [
    { "nombre": "nombreDelComportamiento", "proposito": "..." }
  ]
}
```
Si no hubo adiciones, entrega `{"nuevas_clases": [], "nuevos_comportamientos": []}`.

--- REGLAS ADICIONALES ---

- Prioriza reutilizar clases y comportamientos del registro vigente antes de crear nuevos — el objetivo es que el vocabulario visual/funcional converja, no que crezca indefinidamente sesión tras sesión.
- Mantén consistencia visual con sesiones previas (misma escala tipográfica relativa, misma paleta si ya existen clases de color en el registro).
- Contenido por lámina: prioriza legibilidad en pantalla — listas y bloques cortos por encima de párrafos largos, salvo que el `tipo` de la lámina sea explícitamente narrativo/cita.
- Los `insumos` de cada lámina (tablas, figuras, ecuaciones, código, resultados) deben integrarse fielmente al contenido real provisto en el plan — no inventar datos, cifras ni resultados que no estén ahí.