#importar libreria de faker

from faker import Faker

faker = Faker("es_Mx")
print("Gnerando datos Dummy con faker")
print(f"nombre: {faker.name()}")
print(f"Direccion: {faker.address()}")
print(f"Telefono: {faker.phone_number()}")
print(f"Email: {faker.email()}")