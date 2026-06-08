"""
Materia: Programación Estructurada
Laboratorio: Descomposición de Problemas con IA
Alumno: jetro Sebastián García Sánchez
"""

# ==========================================
# IMPORTACIÓN DE BIBLIOTECAS (Biblioteca Estándar)
# ==========================================

import sys


# ==========================================
# FUNCIONES GENERADAS POR IA
# ==========================================

def limpiar_lecturas(lista_datos):
    """
    Filtra las lecturas del sensor y conserva únicamente
    los valores entre 0.0 y 100.0 inclusive.

    Parámetro:
        lista_datos (list): Lista de números flotantes.

    Retorna:
        list: Lista con lecturas válidas.
    """
    lecturas_validas = []

    for dato in lista_datos:
        if dato >= 0.0 and dato <= 100.0:
            lecturas_validas.append(dato)

    return lecturas_validas


def calcular_alertas(lista_filtrada, umbral_critico):
    """
    Cuenta cuántas lecturas están por debajo del umbral crítico.

    Parámetros:
        lista_filtrada (list): Lista de lecturas válidas.
        umbral_critico (float): Distancia crítica.

    Retorna:
        int: Número total de alertas.
    """
    total_alertas = 0

    for lectura in lista_filtrada:
        if lectura < umbral_critico:
            total_alertas += 1

    return total_alertas


def generar_log_sistema(total_alertas):
    """
    Genera un mensaje de estado del sistema.

    Parámetro:
        total_alertas (int): Cantidad de alertas detectadas.

    Retorna:
        str: Mensaje de log formateado.
    """
    sistema_operativo = sys.platform

    if total_alertas > 3:
        accion = "ABORTAR"
    else:
        accion = "PERMITIDA"

    log = (
        f"[SISTEMA {sistema_operativo}] "
        f"Alertas críticas encontradas: {total_alertas}. "
        f"Acción: {accion}"
    )

    return log


# ==========================================
# PROGRAMA PRINCIPAL
# ==========================================

if __name__ == "__main__":

    # Datos simulados de telemetría
    lecturas_raw = [12.5, -5.0, 88.2, 120.1, 1.2, 0.0, 45.6, 2.5]

    UMBRAL = 3.0

    print("=== SISTEMA DE TELEMETRÍA DE AGENTE AUTÓNOMO ===\n")

    lecturas_limpias = limpiar_lecturas(lecturas_raw)

    total_alertas = calcular_alertas(lecturas_limpias, UMBRAL)

    log_final = generar_log_sistema(total_alertas)

    print(log_final)


"""
========================================================
EVIDENCIAS DE CONTROL DE CALIDAD
========================================================

1. PROMPT UTILIZADO

Actúa como un programador experto en Python Estructurado.
Escribe el código de una función llamada limpiar_lecturas.
Recibe como parámetro una lista de números flotantes y debe
retornar una nueva lista con los valores entre 0.0 y 100.0.
Restricciones estrictas:
1. No utilices programación orientada a objetos.
2. No utilices manejo de excepciones (try-except).
3. Utiliza únicamente estructuras básicas.
4. Incluye documentación mediante Docstring descriptivo.

--------------------------------------------------------

2. TABLA DE PRUEBA DE ESCRITORIO

Caso de prueba:

lecturas_raw = [-10.0, 150.0, -5.5, 120.0]
UMBRAL = 3.0

Paso 1:
limpiar_lecturas()
Resultado:
[]

Paso 2:
calcular_alertas([], 3.0)
Resultado:
0

Paso 3:
generar_log_sistema(0)

Resultado:
[SISTEMA win32] Alertas críticas encontradas: 0.
Acción: PERMITIDA

--------------------------------------------------------

3. AUDITORÍA DE CÓDIGO

La IA inicialmente utilizó comprensión de listas:

lecturas_validas = [dato for dato in lista_datos
                    if 0.0 <= dato <= 100.0]

Aunque es válida en Python, es una sintaxis más avanzada
que no hemos visto en clase.

Para mantener un diseño estructurado básico, se modificó
el código utilizando un ciclo for tradicional y el método
append().

No se utilizaron bibliotecas externas, programación
orientada a objetos ni bloques try-except.
"""