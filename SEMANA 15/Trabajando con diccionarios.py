# --- Programación Orientada a Objetos para el Promedio Semanal del Clima ---

class ClimaDiario:
    """
    Representa la información del clima para un día específico.
    """
    def __init__(self, dia, temperatura=None):
        self._dia = dia  # Atributo protegido para el día
        self._temperatura = temperatura # Atributo protegido para la temperatura

    @property
    def dia(self):
        """Getter para el día."""
        return self._dia

    @property
    def temperatura(self):
        """Getter para la temperatura."""
        return self._temperatura

    @temperatura.setter
    def temperatura(self, value):
        """Setter para la temperatura con validación."""
        if not isinstance(value, (int, float)):
            raise ValueError("La temperatura debe ser un número.")
        self._temperatura = value

    def __str__(self):
        """Representación en cadena del objeto ClimaDiario."""
        return f"Día: {self.dia}, Temperatura: {self.temperatura}°C"

class ClimaSemanal:
    """
    Gestiona la información del clima para toda la semana.
    """
    def __init__(self):
        # Inicializa una lista de objetos ClimaDiario para cada día de la semana
        self._dias = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
        self.clima_dias = [ClimaDiario(dia) for dia in self._dias]

    def ingresar_temperaturas(self):
        """
        Permite al usuario ingresar las temperaturas para cada día de la semana.
        """
        print("Ingrese la temperatura para cada día de la semana:")
        for i, clima_dia in enumerate(self.clima_dias):
            while True:
                try:
                    temp = float(input(f"Temperatura del {clima_dia.dia}: "))
                    clima_dia.temperatura = temp  # Usa el setter con validación
                    break
                except ValueError:
                    print("Entrada inválida. Por favor, ingrese un número.")
                except Exception as e:
                    print(f"Ocurrió un error: {e}")

    def calcular_promedio_semanal(self):
        """
        Calcula el promedio de las temperaturas semanales.
        Retorna:
            float: El promedio de las temperaturas.
        """
        temperaturas_validas = [cd.temperatura for cd in self.clima_dias if cd.temperatura is not None]
        if not temperaturas_validas:
            return 0.0
        return sum(temperaturas_validas) / len(temperaturas_validas)

    def mostrar_temperaturas(self):
        """Muestra las temperaturas ingresadas para cada día."""
        print("\nTemperaturas diarias ingresadas:")
        for clima_dia in self.clima_dias:
            print(clima_dia)

def main_poo():
    """
    Función principal para ejecutar el programa en el enfoque de POO.
    """
    print("--- Cálculo del Promedio Semanal del Clima (Programación Orientada a Objetos) ---")
    clima_semanal = ClimaSemanal()
    clima_semanal.ingresar_temperaturas()
    clima_semanal.mostrar_temperaturas()
    promedio = clima_semanal.calcular_promedio_semanal()
    print(f"El promedio semanal de la temperatura es: {promedio:.2f}°C")

if __name__ == "__main__":
    main_poo()