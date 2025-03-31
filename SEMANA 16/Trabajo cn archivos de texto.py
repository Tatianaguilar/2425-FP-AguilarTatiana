# Escritura de Archivo de Texto
try:
    # Abre el archivo 'my_notes.txt' en modo escritura ('w').
    # Si el archivo no existe, se crea. Si existe, su contenido se sobrescribe.
    with open("my_notes.txt", "w") as archivo:
        # Escribe tres líneas de notas personales en el archivo.
        archivo.write("Recordatorio: Asistir a la cita medica el Lunes.\n")
        archivo.write("Idea para el proyecto: Desarrollar una aplicación de lista de tareas.\n")
        archivo.write("Nota importante: Revisar la tutoria de la clase de Python.\n")
    print("Se han escrito las notas en el archivo 'my_notes.txt'")
except Exception as e:
    print(f"Ocurrió un error al escribir en el archivo: {e}")

# Lectura de Archivo de Texto
try:
    # Abre el archivo 'my_notes.txt' en modo lectura ('r').
    with open("my_notes.txt", "r") as archivo:
        print("\nContenido del archivo 'my_notes.txt':")
        # Lee el archivo línea por línea utilizando readline().
        linea = archivo.readline()
        while linea:
            # Muestra cada línea leída en la consola.
            print(linea.strip())  # .strip() elimina los espacios en blanco al inicio y final, incluyendo el salto de línea.
            linea = archivo.readline()
except FileNotFoundError:
    print("El archivo 'my_notes.txt' no fue encontrado.")
except Exception as e:
    print(f"Ocurrió un error al leer el archivo: {e}")

# El bloque 'with open(...)' asegura que el archivo se cierre automáticamente
# al salir del bloque, incluso si ocurren errores. Por lo tanto, no es necesario
# cerrar el archivo explícitamente con archivo.close() en este caso.