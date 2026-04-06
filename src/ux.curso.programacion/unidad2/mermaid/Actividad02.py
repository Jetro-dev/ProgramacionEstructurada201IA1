def calcular_factorial():
 N = int(input("Ingresa un número: "))

 factorial = 1
 i = 1

 while i <= N:

     factorial = factorial * i

     i = i + 1

 print(factorial)

def main():
   calcular_factorial()
if __name__ == "__main__":
    main()
           