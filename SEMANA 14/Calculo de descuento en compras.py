# Definir la función para calcular el descuento
def calcular_descuento(monto_total, porcentaje_descuento=17):
    descuento = (porcentaje_descuento / 100) * monto_total
    return descuento


# Programa principal
def main():
    # Primer caso: Usando el valor predeterminado de descuento (17%)
    monto_total_1 = 690  # Ejemplo de monto total
    descuento_1 = calcular_descuento(monto_total_1)
    monto_final_1 = monto_total_1 - descuento_1
    print(f"Compra de un Iphone 13: Monto total: {monto_total_1} - Descuento: {descuento_1} = Monto final a pagar: {monto_final_1}")

    # Segundo caso: Proporcionando un porcentaje de descuento específico
    monto_total_2 = 860  # Ejemplo de monto total
    porcentaje_descuento_2 = 17  # Descuento del 17%
    descuento_2 = calcular_descuento(monto_total_2, porcentaje_descuento_2)
    monto_final_2 = monto_total_2 - descuento_2
    print(f"Compra de un Iphone 14 pro: Monto total: {monto_total_2} - Descuento: {descuento_2} = Monto final a pagar: {monto_final_2}")


# Llamar a la función principal
if __name__ == "__main__":
    main()