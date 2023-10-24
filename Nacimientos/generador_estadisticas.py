import json
import numpy as np

# Cargar los datos del archivo JSON
with open('nacimientos.json', 'r') as f:
    data = json.load(f)

sexos = data['sexos']
meses = data['meses']
nacimientos = data['nacimientos']

# Inicializar listas para almacenar las nacimientos por sexo y por mes
nacimientos_por_sexo = {sexo: [] for sexo in sexos}
nacimientos_por_mes = {mes: [] for mes in meses}

# Extraer los datos de nacimientos por sexo y por mes
for sexo in sexos:
    for ano in nacimientos[sexo].keys():
        for mes in meses:
            nacimientos_por_sexo[sexo].append(nacimientos[sexo][ano][mes])
            nacimientos_por_mes[mes].append(nacimientos[sexo][ano][mes])

# Calcular estadísticas descriptivas con numpy
estadisticas_sexo = {}
estadisticas_mes = {}

for sexo, nacimientos in nacimientos_por_sexo.items():
    estadisticas_sexo[sexo] = {
        'Promedio': float(np.mean(nacimientos)),
        'Minimo': int(np.min(nacimientos)),
        'Maximo': int(np.max(nacimientos)),
        'Total': int(np.sum(nacimientos)),
        'DesviacionEstandar': float(np.std(nacimientos)),
        'Mediana': float(np.median(nacimientos))
    }

for mes, nacimientos in nacimientos_por_mes.items():
    estadisticas_mes[mes] = {
        'Promedio': float(np.mean(nacimientos)),
        'Minimo': int(np.min(nacimientos)),
        'Maximo': int(np.max(nacimientos)),
        'Total': int(np.sum(nacimientos)),
        'DesviacionEstandar': float(np.std(nacimientos)),
        'Mediana': float(np.median(nacimientos))
    }

# Guardar las estadísticas descriptivas en un archivo JSON
with open('estadisticas_sexo.json', 'w') as f:
    json.dump(estadisticas_sexo, f, indent=4)

with open('estadisticas_mes.json', 'w') as f:
    json.dump(estadisticas_mes, f, indent=4)

print("Estadísticas descriptivas generadas y guardadas exitosamente en archivos JSON.")
