import json
import random

# Listado del sexo
sexos = ["Femenino", "Masculino", "Indeterminado"]

# Listado de meses
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

# Diccionario para almacenar los nacimientos por año
nacimientos = {}

# Generar nacimientos aleatorias para los años 2020, 2021, y 2022
for sexo in sexos:
    nacimientos[sexo] = {}
    for ano in range(2020, 2023):
        nacimientos[sexo][ano] = {}
        for mes in meses:
            # Generar un número aleatorio de nacimientos
            if sexo == "Femenino":
                nacimientos[sexo][ano][mes] = random.randint(36470, 56470)
            elif sexo == "Masculino" :
                nacimientos[sexo][ano][mes] = random.randint(38580, 58580)
            else:
                nacimientos[sexo][ano][mes] = random.randint(5, 10)

# Crear el archivo JSON con los datos de nacimientos
data = {
    "sexos": sexos,
    "meses": meses,
    "nacimientos": nacimientos
}

with open('nacimientos.json', 'w') as f:
    json.dump(data, f, indent=4)

print("Archivo de nacimientos generado exitosamente.")
