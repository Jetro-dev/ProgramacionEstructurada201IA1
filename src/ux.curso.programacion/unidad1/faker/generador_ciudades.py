#importar libreria de faker

from faker import Faker

fake = Faker("es_MX")

# 1 declaracion de un vector vacio 
ciudades_ia = []

#2 operacion de llamado(ciclo)
for _ in range(5):
    ciudades_ia.append(fake.city())

#3. escritura de arreglos (mostrar resultados)
print("\n--- DATASET DE CIUDADES GENERANDO---")
for i in range (len(ciudades_ia)):
    print(f"Registro {i+1}: {ciudades_ia[i]}")