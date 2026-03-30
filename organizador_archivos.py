import os
import shutil

def organizar_archivos(ruta_carpeta):
    if not os.path.exists(ruta_carpeta):
        print("La carpeta no existe.")
        return

    for archivo in os.listdir(ruta_carpeta):
        ruta_archivo = os.path.join(ruta_carpeta, archivo)

        # Ignorar carpetas
        if os.path.isdir(ruta_archivo):
            continue

        # Obtener extensión
        extension = archivo.split(".")[-1].lower()

        # Crear carpeta para la extensión
        carpeta_destino = os.path.join(ruta_carpeta, extension)
        os.makedirs(carpeta_destino, exist_ok=True)

        # Mover archivo
        shutil.move(ruta_archivo, os.path.join(carpeta_destino, archivo))

    print("Organización completada.")
