"""
Materia: Programación Estructurada
Laboratorio: Refactorización y Análisis de Código (Parte II)
Alumno: Jetro Sebastián García Sánchez
"""

import random
import statistics 

# =====================================================================
# RETO 1: Formateador de Nombres de Usuario para Discord
# - Se reemplazó la limpieza manual por strip().
# - Se reemplazó la conversión manual por capitalize().
# - Código más corto, legible y eficiente.
# =====================================================================
def limpiar_nombre_usuario(nombre_sucio):
    return nombre_sucio.strip().capitalize()


# =====================================================================
# RETO 2: Buscador de Palabras Prohibidas
# - Se reemplazó la búsqueda letra por letra por el operador in.
# - Python ya incluye esta funcionalidad.
# =====================================================================
def contiene_palabra_bloqueada(mensaje_chat, palabra_prohibida):
    return palabra_prohibida in mensaje_chat


# =====================================================================
# RETO 3: Generador de Contraseñas Temporales
# - Se utiliza random.choice().
# - Se utiliza join() para evitar concatenaciones repetitivas.
# =====================================================================
def generar_clave_temporal():
    caracteres_validos = "ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnpqrstuvwxyz23456789"

    return "".join(
        random.choice(caracteres_validos)
        for _ in range(8)
    )


# =====================================================================
# RETO 4: Mediana de Latencia
# - Se reemplazó el ordenamiento burbuja manual.
# - Se utiliza statistics.median().
# - Código más profesional y eficiente.
# =====================================================================
def calcular_mediana_latencia(lista_pings):
    return statistics.median(lista_pings)


def main():
    print("--- Probando Código Refactorizado (Parte II) ---")

    print("Usuario limpio:",
          [limpiar_nombre_usuario("   luNA_eDUaRDo  ")])

    msg = "No digas malas palabras en este servidor"
    print("¿Tiene groserías?:",
          contiene_palabra_bloqueada(msg, "malas"))

    print("Clave generada por el sistema:",
          generar_clave_temporal())

    pings_servidor = [120, 45, 80, 23, 150, 62]
    print("Mediana de latencia encontrada:",
          calcular_mediana_latencia(pings_servidor))


if __name__ == "__main__":
    main()