import json
import random

productos = ["Gaseosas", "Crispetas", "HotDog", "Chocolatina", "Nachos", "Papas", "Agua"]
meses = ["ENE", "FEB", "MAR", "ABR", "MAY", "JUN", "JUL", "AGO", "SEP", "OCT", "NOV", "DIC"]

ventas = {}
for producto in productos:
    ventas[producto]= {}
    for anio in range(2019, 2023):
        ventas[producto][anio] = {}
        for mes in meses:
            if producto == "Crispetas":
                ventas[producto][anio][mes] = random.randint(850, 1500)
            else:
                ventas[producto][anio][mes] = random.randint(50, 1000)
                

#Generar el Archivo JSON
data = {"productos": productos,
        "meses": meses,
        "ventas": ventas
}

with open('ventas.json','w') as file:
    json.dump(data, file, indent=4)

print('datos dummis GENERADO!')
