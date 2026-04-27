def procesar_pregunta(mensaje_usuario):
    conocimiento = {
        # Funciones básicas
        "print": "Función que muestra información en la consola o salida estándar.",

        # Conceptos de Programación Estructurada
        "algoritmo": "Es una serie de pasos ordenados y finitos para resolver un problema.",

        # Estructuras de control
        "if": "Estructura de control que permite tomar decisiones según una condición.",
        "while": "Estructura de repetición que ejecuta un bloque de código mientras una condición sea verdadera.",
        "for": "Estructura de repetición que itera sobre una secuencia de datos.",

        # Tipos de datos
        "int": "Tipo de dato entero, representa números sin decimales.",
        "float": "Tipo de dato numérico con decimales.",
        "string": "Tipo de dato que representa texto.",
        "bool": "Tipo de dato que solo puede ser verdadero o falso.",

        # Funciones y modularidad
        "funcion": "Bloque de código reutilizable que realiza una tarea específica.",
        "modularidad": "Dividir un programa en partes más pequeñas para facilitar su mantenimiento.",

        # Operadores
        "operadores": "Símbolos que permiten realizar operaciones como suma, resta o comparaciones.",
        "+": "Operador de suma.",
        "-": "Operador de resta.",
        "*": "Operador de multiplicación.",
        "/": "Operador de división."
    }

    mensaje_usuario = mensaje_usuario.lower()

    # Lógica de búsqueda
    for clave in conocimiento:
        if clave in mensaje_usuario:
            return conocimiento[clave]

    return "Lo siento, aún no sé qué es eso. ¡Pregúntame sobre programación!"


def main():
    print("¡Hola! Soy tu asistente de programación. Pregúntame sobre conceptos básicos.")
    
    while True:
        user_input = input("Alumno -> ")
        
        if user_input.lower() == "salir":
            break

        respuesta = procesar_pregunta(user_input)
        print(f"Bot -> {respuesta}")


if __name__ == "__main__":
    main()