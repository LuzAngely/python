import json
import numpy as np
import matplotlib.pyplot as plt  #ejecutar comando: pip install matplotlib

# Cargar los datos del archivo JSON
with open('ventas.json', 'r') as f:
    data = json.load(f)

productos = data['productos']
meses = data['meses']
ventas = data['ventas']

# Procesar los datos y calcular las estadísticas descriptivas por producto y por mes
estadisticas_por_producto = {}
estadisticas_por_mes = {mes: [] for mes in meses}

for venta in ventas:
    producto = venta[productos]
    ventas_por_mes = [venta[anio][mes] for anio in venta.keys() if anio != 'producto' for mes in meses]
    estadisticas_por_producto[producto] = {
        'Promedio': np.mean(ventas_por_mes),
        'Mínimo': np.min(ventas_por_mes),
        'Máximo': np.max(ventas_por_mes),
        'Total': np.sum(ventas_por_mes),
    }
    for mes, valor in zip(meses, ventas_por_mes):
        estadisticas_por_mes[mes].append(valor)

# Mostrar las estadísticas descriptivas por producto
print("Estadísticas descriptivas por producto:")
for producto, estadisticas in estadisticas_por_producto.items():
    print(f"Producto: {producto}")
    for clave, valor in estadisticas.items():
        print(f"{clave}: {valor}")
    print()

# Mostrar las estadísticas descriptivas por mes
print("Estadísticas descriptivas por mes:")
for mes, valores in estadisticas_por_mes.items():
    print(f"Mes: {mes}")
    print(f"Promedio: {np.mean(valores)}")
    print(f"Mínimo: {np.min(valores)}")
    print(f"Máximo: {np.max(valores)}")
    print(f"Total: {np.sum(valores)}")
    print()

# Crear el gráfico de barras para el promedio de ventas por producto
valores_productos = [estadisticas['Promedio'] for estadisticas in estadisticas_por_producto.values()]

plt.figure(figsize=(10, 5))
plt.bar(productos, valores_productos, color='skyblue')
plt.xlabel('Productos')
plt.ylabel('Promedio de Ventas')
plt.title('Promedio de Ventas por Producto')
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()

# Crear el gráfico de barras para las ventas totales por mes
valores_meses = [np.sum(valores) for valores in estadisticas_por_mes.values()]

plt.figure(figsize=(10, 5))
plt.bar(meses, valores_meses, color='lightcoral')
plt.xlabel('Meses')
plt.ylabel('Ventas Totales')
plt.title('Ventas Totales por Mes')
plt.tight_layout()

plt.show()
