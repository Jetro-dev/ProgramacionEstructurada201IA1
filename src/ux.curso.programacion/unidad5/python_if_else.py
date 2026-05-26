def verificar_numero(n):
    if n % 2 != 0:
        return "Weird"
    elif n % 2 == 0 and 2 <= n <= 5:
        return "Not Weird"
    elif n % 2 == 0 and 6 <= n <= 20:
        return "Weird"
    else:
        return "Not Weird"


def main():
    print("SISTEMA IF-ELSE")
    print("----------------")

    n = int(input("Ingrese un número: "))

    resultado = verificar_numero(n)

    print(f"Resultado: {resultado}")


if __name__ == "__main__":
    main()