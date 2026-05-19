print("funciones externas (biblioteca)")

# 1. IMPORTACIÓN
import numpy as np


def procesar_estadisticas(lista_mensajes):
    """
    Función que recibe datos y utiliza funciones externas de
    la biblioteca NumPy para procesarlos.
    """

    promedio = np.mean(lista_mensajes)

    pico_maximo = np.max(lista_mensajes)

    desviacion = np.std(lista_mensajes)

    mediana = np.median(lista_mensajes)

    return promedio, pico_maximo, desviacion, mediana


def main():

    # --- Programa Principal ---
    datos_servidor = [15, 42, 88, 30, 120, 55, 72, 20]

    # Recibir los 4 valores correctamente
    prom, maximo, ds, mediana = procesar_estadisticas(datos_servidor)

    print("=== REPORTE DE ACTIVIDAD DEL SERVIDOR ===")
    print(f"Promedio de mensajes por hora: {prom:.2f}")
    print(f"Pico de actividad registrado: {maximo} mensajes")
    print(f"Variabilidad del tráfico (Desviación): {np.round(ds, 2)}")
    print(f"Mediana del tráfico: {mediana:.2f}")

    #4. ¿Qué sucede si intentas usar np.mean() sin haber hecho el  import al principio del archivo?  Nos mandaria un error de NameError.


if __name__ == "__main__":
    main()