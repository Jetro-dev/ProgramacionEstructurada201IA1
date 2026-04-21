def validar_fecha(dia, mes, año):
    # Validar mes
    if mes < 1 or mes > 12:
        return "Fecha inválida"

    es_bisiesto = (año % 400 == 0) or (año % 4 == 0 and año % 100 != 0)

    if mes == 2:
        if es_bisiesto:
            max_dias = 29
        else:
            max_dias = 28
    elif mes in [4, 6, 9, 11]:
        max_dias = 30
    else:
        max_dias = 31

    
    if 1 <= dia <= max_dias:
        return "Fecha válida"
    else:
        return "Fecha inválida"

dia = int(input("Ingrese día: "))
mes = int(input("Ingrese mes: "))
año = int(input("Ingrese año: "))




def main():
    print(validar_fecha(dia, mes, año))

if __name__=="__main__":
    main()
