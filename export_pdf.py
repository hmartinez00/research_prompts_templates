# ==============================================================================
# SCRIPT DE AUTOMATIZACIÓN: EXPORTACIÓN Y RENOMBRADO CON CONTROL DE EXISTENCIA
# ==============================================================================
import os
import shutil

def exportar_y_renombrar_pdf():
    # 1. Obtener las rutas del entorno de trabajo actual
    current_dir = os.getcwd()
    dir_name = os.path.basename(current_dir)
    parent_dir = os.path.dirname(current_dir)
    
    # 2. Definir el archivo de origen (debe ser el main.pdf compilado)
    source_pdf = "main.pdf"
    
    # Control de existencia del entregable principal en el directorio actual
    if not os.path.exists(source_pdf):
        print(f"❌ Error: No se encontró el archivo '{source_pdf}' en el directorio actual.")
        print("Asegúrese de haber compilado exitosamente el proyecto LaTeX antes de ejecutar este script.")
        return

    # 3. Formatear el nuevo nombre basado en el directorio del proyecto
    new_pdf_name = f"{dir_name}.pdf"
    target_path = os.path.join(parent_dir, new_pdf_name)
    
    # 4. CONTROL DE EXISTENCIA: Verificar si el archivo ya existe en el directorio padre
    archivo_previo_existe = os.path.exists(target_path)
    
    try:
        # Si existe, intentamos asegurar que no haya conflictos de sobreescritura extraños
        if archivo_previo_existe:
            try:
                os.remove(target_path) # Remover el archivo viejo antes de copiar el nuevo
            except PermissionError:
                print(f"❌ Error de permisos: El archivo de destino '{new_pdf_name}' ya existe en el directorio padre y está abierto/bloqueado por otro programa.")
                return

        # 5. Ejecutar la copia física y traslado al directorio padre
        shutil.copy2(source_pdf, target_path)
        
        if archivo_previo_existe:
            print(f"🔄 ¡Actualización exitosa! El archivo previo fue reemplazado:")
        else:
            print(f"✅ ¡Exportación exitosa! Nuevo archivo generado:")
            
        print(f"   • Ubicación: {target_path}")

    except Exception as e:
        print(f"❌ Fallo crítico durante la exportación: {str(e)}")

if __name__ == "__main__":
    exportar_y_renombrar_pdf()