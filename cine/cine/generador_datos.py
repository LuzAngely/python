import json
import random

# Lista de productos de confitería
productos = ["Gaseosas", "Crispetas", "HotDog", "Gomitas", "Chocolates", "Helados", "Nachos", "Cafe", "Dulces", "Churros"]

# Lista de meses
meses = ["ENE", "FEB", "MAR", "ABR", "MAY", "JUN", "JUL", "AGO", "SEP", "OCT", "NOV", "DIC"]

# Diccionario para almacenar las ventas por producto y por año
ventas = {}

# Generar ventas aleatorias para los años 2020, 2021, 2022 y 2023
for producto in productos:
    ventas[producto] = {}
    for anio in range(2020, 2024):
        ventas[producto][anio] = {}
        for mes in meses:
            # Generar un número aleatorio de ventas entre 100 y 1000
            if producto == "Crispetas":
                ventas[producto][anio][mes] = random.randint(2500, 3000)
            elif producto == "Gaseosas" :
                ventas[producto][anio][mes] = random.randint(1000, 2000)
            elif producto == "Helados":
                ventas[producto][anio][mes] = random.randint(10, 30)
            else:
                ventas[producto][anio][mes] = random.randint(100, 500)

# Crear el archivo JSON con los datos de ventas
data = {
    "productos": productos,
    "meses": meses,
    "ventas": ventas
}

with open('ventas.json', 'w') as f:
    json.dump(data, f, indent=4)

print("Archivo de ventas generado exitosamente.")
