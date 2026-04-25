def procesar_pregunta(mensaje_usuario):
    conocimiento = {
        "print": "Función que muestra información en la consola o salida estándar.",

        # Conceptos de Programación Estructurada
        "algoritmo": "Es una serie de pasos ordenados y finitos para resolver un problema."
    }

    # 3. Lógica de búsqueda
    for clave in conocimiento:
        if clave in mensaje_usuario:
            return conocimiento[clave]

    return "Lo siento, aún no sé qué es eso. ¡Pregúntame sobre variables, algoritmos, etc.!"


def main():
    print("¡Hola! Soy tu asistente de programación. Pregúntame sobre variables, algoritmos, etc.")
    
    while True:
        user_input = input("Alumno -> ")
        
        if user_input.lower() == "salir":
            break

        respuesta = procesar_pregunta(user_input)
        print(f"Bot -> {respuesta}")


# Prueba local (offline)
if __name__ == "__main__":
    main()