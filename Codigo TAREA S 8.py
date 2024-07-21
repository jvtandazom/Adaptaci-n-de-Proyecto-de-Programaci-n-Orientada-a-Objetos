import os


def mostrar_codigo(ruta_script):
    """
    Muestra el contenido del archivo especificado.

    :param ruta_script: Ruta del script a mostrar.
    """
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")


def crear_nuevo_script(ruta_script):
    """
    Crea un nuevo script con contenido predeterminado.

    :param ruta_script: Ruta donde se creará el nuevo script.
    """
    try:
        with open(ruta_script, 'w') as archivo:
            contenido_predeterminado = "# Nuevo script\nprint('Hola, mundo!')"
            archivo.write(contenido_predeterminado)
            print(f"Script creado en {ruta_script}")
    except Exception as e:
        print(f"Ocurrió un error al crear el archivo: {e}")


def mostrar_menu():
    """
    Muestra el menú principal del dashboard.
    """
    ruta_base = os.path.dirname(__file__)

    opciones = {
        '1': 'Unidad 1/1.2. Tecnicas de Programacion/1.2-1. Ejemplo Tecnicas de Programacion.py',
        # Agrega aquí el resto de las rutas de los scripts
        '2': 'Crear nuevo script'  # Opción para crear un nuevo script
    }

    while True:
        print("\nMenú Principal - Dashboard")
        # Información personalizada
        print("Universidad Estatal Amazónica")
        print("Nombre: Jonathan Tandazo")
        print("Clase: Programación\n")

        # Imprime las opciones del menú
        for key in opciones:
            print(f"{key} - {opciones[key]}")
        print("0 - Salir")

        eleccion = input("Elige una opción o '0' para salir: ")
        if eleccion == '0':
            break
        elif eleccion == '2':
            # Solicita la ruta para el nuevo script y lo crea
            nuevo_script_ruta = input("Ingresa la ruta para el nuevo script: ")
            crear_nuevo_script(os.path.join(ruta_base, nuevo_script_ruta))
        elif eleccion in opciones:
            # Muestra el código del script seleccionado
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            mostrar_codigo(ruta_script)
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")


if __name__ == "__main__":
    mostrar_menu()