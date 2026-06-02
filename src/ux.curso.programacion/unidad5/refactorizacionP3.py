"""
Materia: Programación Estructurada
Laboratorio: Refactorización y Análisis de Código (Parte III)
Alumno: Jetro Sebastián García Sánchez
"""

import math

# =====================================================================
# RETO 1: Inicializador de Tablero de Juego:
# - Se reemplazó la reutilización de la misma fila por una comprensión
#   de listas para crear filas independientes.
# - Se eliminaron los ciclos redundantes de limpieza.
# =====================================================================
def inicializar_tablero_vacio():
    return [[0 for _ in range(4)] for _ in range(4)]


# =====================================================================
# RETO 2: Recortador de Valores Atípicos
# - Se reemplazó la lógica condicional por min() y max().
# - Código más compacto y fácil de leer.
# =====================================================================
def limitar_senal_sensor(valor_lectura, minimo, maximo):
    return max(minimo, min(valor_lectura, maximo))


# =====================================================================
# RETO 3: Buscador del Valor Más Cercano a Cero
# - Se utiliza math.fabs() para obtener el valor absoluto.
# - Se utiliza min() para encontrar el menor valor absoluto.
# - Se elimina el uso de números arbitrarios como 999999.99.
# =====================================================================
def buscar_error_minimo(lista_errores):
    return min(math.fabs(error) for error in lista_errores)


# =====================================================================
# RETO 4: Filtro de Valores Únicos
# - Se utiliza set() para eliminar duplicados.
# - Se convierte nuevamente a lista para mantener el mismo tipo de dato.
# =====================================================================
def depurar_usuarios_repetidos(lista_ids):
    return list(set(lista_ids))


def main():
    print("--- Probando Código Refactorizado (Parte III) ---")

    tablero_ia = inicializar_tablero_vacio()
    print("Tablero inicializado de 4x4:")
    for fila in tablero_ia:
        print(fila)

    print(
        "Lectura recortada (125.4 en rango 0-100):",
        limitar_senal_sensor(125.4, 0.0, 100.0)
    )

    errores_entrenamiento = [0.45, -0.12, 0.89, -0.03, 0.22]
    print(
        "El error más cercano a cero es:",
        buscar_error_minimo(errores_entrenamiento)
    )

    ids_discord = [4521, 8892, 4521, 1022, 8892, 9931]
    print(
        "Lista de IDs únicas filtradas:",
        depurar_usuarios_repetidos(ids_discord)
    )


if __name__ == "__main__":
    main()