def normalizar_mensaje(texto):
    return texto.lower().strip()


def detectar_intencion(mensaje):
    if "encender" in mensaje or "activar" in mensaje or "reproducir" in mensaje:
        return "COMANDO DE ACCIÓN"
    elif "ayuda" in mensaje or "error" in mensaje or "fallo" in mensaje:
        return "REPORTE DE SOPORTE"
    else:
        return "CONSULTA GENERAL"


def main():
    mensaje_original = input("Ingrese comando de voz: ")

    mensaje_limpio = normalizar_mensaje(mensaje_original)
    categoria = detectar_intencion(mensaje_limpio)
    longitud = len(mensaje_original)

    print("\n--- PROCESANDO POR IA ---\n")
    print(f'Mensaje Normalizado: "{mensaje_limpio}"')
    print(f"Categoría de Intención: {categoria}")
    print(f"Longitud del mensaje: {longitud} caracteres")


if __name__ == "__main__":
    main()