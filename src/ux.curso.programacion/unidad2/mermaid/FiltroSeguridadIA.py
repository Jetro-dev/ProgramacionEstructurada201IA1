def filtro_seguridad_ia():
    
    LIMITE_SUPERIOR = 100.0
    LIMITE_INFERIOR = 0.0

    
    lectura = float(input("Ingrese la lectura del sensor térmico: "))

    
    if LIMITE_INFERIOR <= lectura <= LIMITE_SUPERIOR:
        dato_normalizado = lectura / LIMITE_SUPERIOR
        print(f"Señal aceptada. Valor normalizado para el modelo: {dato_normalizado}")
    else:
        print("Error: Lectura fuera de rango. La señal se considera ruido.")

    
    print("Fin del proceso de filtrado de datos.")


def main():
    filtro_seguridad_ia()


if __name__ == "__main__":
    main()