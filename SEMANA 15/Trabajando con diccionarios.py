## --- Programación Tradicional para el Promedio Semanal del Clima ---

def obtener_temperaturas_diarias():
    """
    Solicita al usuario las temperaturas para cada día de la semana.
    Retorna una lista de flotantes con las temperaturas.
    """
    temperaturas = []
    dias_semana = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
    print("Ingrese la temperatura para cada día de la semana:")
    for dia in dias_semana:
        while True:
            try:
                temp = float(input(f"Temperatura del {dia}: "))
                temperaturas.append(temp)
                break
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número.")
    return temperaturas

def calcular_promedio_semanal(temperaturas):
    """
    Calcula el promedio de una lista de temperaturas.
    Parámetros:
        temperaturas (list): Una lista de números flotantes.
    Retorna:
        float: El promedio de las temperaturas.
    """
    if not temperaturas:
        return 0.0  # Retorna 0 si la lista está vacía para evitar división por cero
    return sum(temperaturas) / len(temperaturas)

def main_tradicional():
    """
    Función principal para ejecutar el programa en el enfoque tradicional.
    """
    print("--- Cálculo del Promedio Semanal del Clima (Programación Tradicional) ---")
    temps = obtener_temperaturas_diarias()
    promedio = calcular_promedio_semanal(temps)
    print(f"\nLas temperaturas diarias ingresadas fueron: {temps}")
    print(f"El promedio semanal de la temperatura es: {promedio:.2f}°C")

if __name__ == "__main__":
    main_tradicional()