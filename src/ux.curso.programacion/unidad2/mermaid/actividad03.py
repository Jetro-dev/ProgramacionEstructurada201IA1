def numeros_impares():
    N = int(input("Ingresa N: "))
    
    contador = 0
    numero = 1
    
    while contador < N:
        print(numero)
        numero = numero + 2
        contador = contador + 1


def main():
    numeros_impares()
if __name__ == "__main__":
    main()