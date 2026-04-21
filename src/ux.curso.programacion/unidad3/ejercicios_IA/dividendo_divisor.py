def division(dividendo, divisor):
    if divisor == 0:
        return "Error: división por cero"

    cociente = 0
    resto = dividendo

    while resto >= divisor:
        resto = resto - divisor
        cociente = cociente + 1

    return f"Cociente = {cociente}, Resto = {resto}"


dividendo = int(input("Ingrese el dividendo: ")) 
divisor = int(input("Ingrese el divisor: "))



def main():
    print(division(dividendo, divisor))

if __name__=="__main__":
    main()
