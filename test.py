import os

def borrar_archivos_excepto_videos(carpeta):
    archivos_borrados = 0

    for root, _, archivos in os.walk(carpeta):
        for archivo in archivos:
            ruta_archivo = os.path.join(root, archivo)
            if os.path.isfile(ruta_archivo):
                nombre, extension = os.path.splitext(archivo)
                extension = extension.lower()
                if extension in ['.mp4', '.avi', '.mkv']:
                    nuevo_nombre = input(f"Ingrese un nuevo nombre para {archivo}: ")
                    nuevo_nombre_archivo = os.path.join(root, nuevo_nombre + extension)
                    os.rename(ruta_archivo, nuevo_nombre_archivo)
                    print(f"Archivo renombrado: {archivo} a {nuevo_nombre + extension}")
                else:
                    os.remove(ruta_archivo)
                    archivos_borrados += 1
                    print(f"Archivo borrado: {ruta_archivo}")

    print(f"Total de archivos borrados: {archivos_borrados}")


def mover_archivos(carpeta_origen, carpeta_destino):
    archivos_movidos = 0

    for root, _, archivos in os.walk(carpeta_origen):
        for archivo in archivos:
            ruta_archivo = os.path.join(root, archivo)
            if os.path.isfile(ruta_archivo):
                nombre, extension = os.path.splitext(archivo)
                extension = extension.lower()
                if extension in ['.mp4', '.avi', '.mkv']:
                    destino = input(f"Para mover los archivos ingrese 's' para series o 'p' para peliculas {archivo}: ")
                    if destino.lower() == 's':
                        nueva_ruta = os.path.join(carpeta_destino, 'Series', archivo)
                    elif destino.lower() == 'p':
                        nueva_ruta = os.path.join(carpeta_destino, 'Peliculas', archivo)
                    else:
                        print("Destino inválido. El archivo no se moverá.")
                        continue

                    os.rename(ruta_archivo, nueva_ruta)
                    print(f"Archivo {archivo} movido a {nueva_ruta}")
                    archivos_movidos += 1

    print(f"Total de archivos movidos: {archivos_movidos}")

# Configuración
carpeta_origen = "C:\\Users\\cinco\\Downloads"
carpeta_destino = "C:\\Users\\cinco\\Documents"

borrar_archivos_excepto_videos(carpeta_origen)
mover_archivos(carpeta_origen, carpeta_destino)