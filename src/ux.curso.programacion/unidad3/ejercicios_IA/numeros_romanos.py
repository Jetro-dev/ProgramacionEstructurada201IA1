def convertir_a_romano(N):  # ← faltaba este :
    if not isinstance(N, int) or N <= 0 or N >= 1000:
        return "Error: el número debe ser entero positivo menor a 1000"

    valores = [
        (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    ]

    resultado = ""

    while N > 0:
        for valor, simbolo in valores:
            if N >= valor:
                resultado += simbolo
                N -= valor
                break  

    return resultado


def main():
    numero = int(input("Ingrese un número (1-999): "))
    print("Número romano:", convertir_a_romano(numero))


if __name__ == "__main__":
    main()