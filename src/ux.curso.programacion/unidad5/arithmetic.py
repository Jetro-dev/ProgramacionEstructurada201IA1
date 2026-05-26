def operaciones(a, b):
    print(a + b)
    print(a - b)
    print(a * b)


def main():
    print("OPERADORES ARITMÉTICOS")
    print("----------------------")

    a = int(input("Ingrese el primer número: "))
    b = int(input("Ingrese el segundo número: "))

    operaciones(a, b)


if __name__ == "__main__":
    main()