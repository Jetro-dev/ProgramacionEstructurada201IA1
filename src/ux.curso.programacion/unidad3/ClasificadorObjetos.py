# ClasificadorObjetos.py

UMBRAL_PEQUENO = 5.0
UMBRAL_GRANDE = 20.0

def clasificar_objeto():
    dimension = float(input("Ingrese el tamaño del objeto detectado (cm): "))

    if dimension <= 0.0:
        print("Error: Lectura inválida. Verifique el sensor.")

    elif dimension <= UMBRAL_PEQUENO:
        print("Clasificación: Micro-componente (Grado A)")

    elif dimension <= UMBRAL_GRANDE:
        print("Clasificación: Componente Estándar (Grado B)")

    else:
        print("Clasificación: Componente Industrial (Grado C)")
        
        volumen = dimension ** 3
        print("Espacio requerido en contenedor:", volumen, "cm3")

    print("Registro de inspección completado.")


def main():
    clasificar_objeto()


if __name__ == "__main__":
    main()