import datetime

def asistente_logico():
    
    nombre_asistente = "IA-UX"
    print(f"Bienvenido, soy {nombre_asistente}")

    frase = input("¿En qué puedo ayudarte hoy?: ").lower()


    if "hola" in frase or "buenos días" in frase:
        print("¡Hola! Soy tu asistente. Es un gusto saludarte.")

    elif "clima" in frase or "temperatura" in frase:
        print("Consultando el servicio meteorológico... Hoy en Xalapa tendremos un día nublado.")

    elif "hora" in frase or "tiempo" in frase:
        hora_actual = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"La hora actual del sistema es: {hora_actual}")

    else:
        print("Lo siento, todavía no entiendo ese comando. ¿Podrías intentar con otra palabra?")

    print(f"Proceso finalizado. Gracias por usar {nombre_asistente}.")


def main():
    asistente_logico()


if __name__ == "__main__":
    main()