def simulador_login():
    intentos = 0
    clave_correcta = "ABCDE"

    while intentos < 3:
        contrasena = input("Ingrese clave: ")

        if contrasena == clave_correcta:
            print("Acceso Concedido")
            break
        else:
            intentos += 1
            print("Contraseña incorrecta")

    if intentos == 3:
        print("Cuenta bloqueada")


def main():
    simulador_login()


if __name__ == "__main__":
    main()