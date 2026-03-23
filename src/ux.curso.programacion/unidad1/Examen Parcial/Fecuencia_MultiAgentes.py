def sincronizacion():
    agente_A = int (input("Digite La frecuencia en HZ del agente A: "))
    agente_B = int (input("Digite La frecuencia en HZ del agente B: "))

    if (agente_A % agente_B == 0):
        print("La sincronización es perfecta para el intercambio de mensajes")
    elif (agente_B % agente_A == 0):
        print("La sicronización es perfecta para el intercambio de mensajes")
    else:
        print("No hay sicronización")   





def main():
    sincronizacion()
if __name__ == "__main__":
    main()              