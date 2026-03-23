def neurona():
    w = float(input("Ingrese el peso (w): "))
    x = float(input("Ingrese el dato de entrada (x): "))

    Z = w * x

    print(f"El valor de activación Z es: {Z}" )


def main():
    neurona()

if __name__ == "__main__":
    main()