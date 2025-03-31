# Crear un diccionario llamado informacion_personal
informacion_personal = {
    "nombre": "Tatiana Aguilar",
    "edad": 20,
    "ciudad": "Aatuntaqui",
    "profesion": "Estudiante"
}

# Acceder y modificar el valor de la clave "ciudad"
informacion_personal["ciudad"] = "Atuntaqui"

# Agregar una nueva clave-valor al diccionario
informacion_personal["profesion"] = "Desarrolladora de Software"

# Verificar si la clave "telefono" existe en el diccionario
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "123-456-7890"

# Eliminar la clave "edad" del diccionario
del informacion_personal["edad"]

# Imprimir el diccionario final
print(informacion_personal)