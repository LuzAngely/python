import json
import numpy as np

# Cargar los datos del archivo JSON
with open('ventas.json', 'r') as f:
    data = json.load(f)

productos = data['productos']
meses = data['meses']
ventas = data['ventas']

# Inicializar listas para almacenar las ventas por producto y por mes
ventas_por_producto = {producto: [] for producto in productos}
ventas_por_mes = {mes: [] for mes in meses}

# Extraer los datos de ventas por producto y por mes
for producto in productos:
    for anio in ventas[producto].keys():
        for mes in meses:
            ventas_por_producto[producto].append(ventas[producto][anio][mes])
            ventas_por_mes[mes].append(ventas[producto][anio][mes])

# Calcular estadísticas descriptivas con numpy
estadisticas_por_producto = {}
estadisticas_por_mes = {}

for producto, ventas in ventas_por_producto.items():
    estadisticas_por_producto[producto] = {
        'Promedio': float(np.mean(ventas)),
        'Minimo': int(np.min(ventas)),
        'Maximo': int(np.max(ventas)),
        'Total': int(np.sum(ventas)),
        'DesviacionEstandar': float(np.std(ventas)),
        'Mediana': float(np.median(ventas))
    }

for mes, ventas in ventas_por_mes.items():
    estadisticas_por_mes[mes] = {
        'Promedio': float(np.mean(ventas)),
        'Minimo': int(np.min(ventas)),
        'Maximo': int(np.max(ventas)),
        'Total': int(np.sum(ventas)),
        'DesviacionEstandar': float(np.std(ventas)),
        'Mediana': float(np.median(ventas))
    }

# Guardar las estadísticas descriptivas en un archivo JSON
with open('estadisticas_por_producto.json', 'w') as f:
    json.dump(estadisticas_por_producto, f, indent=4)

with open('estadisticas_por_mes.json', 'w') as f:
    json.dump(estadisticas_por_mes, f, indent=4)

print("Estadísticas descriptivas generadas y guardadas exitosamente en archivos JSON.")
