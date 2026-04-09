def calculo_semanas_trabajadas():
    total_acumulado = 0
    semanas = 0
    meta = 2500

    while total_acumulado < meta:
        print(f"Semana {semanas + 1}")
        salario_semanal = float(input("Ingresa el salario semanal: "))
        
        total_acumulado = total_acumulado + salario_semanal
        semanas = semanas + 1

    semanas_trabajadas = semanas
    print("Semanas trabajadas:", semanas_trabajadas)
    print("Dinero total recaudado:", total_acumulado)

    
   
def main():
    calculo_semanas_trabajadas()
if __name__ == "__main__":
    main()
