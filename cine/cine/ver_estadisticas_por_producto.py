import json
import matplotlib.pyplot as plt

# Cargar los datos del archivo JSON
with open('estadisticas_por_producto.json', 'r') as f:
    estadisticas_por_producto = json.load(f)

# Extraer los nombres de los productos y las estadísticas
productos = list(estadisticas_por_producto.keys())
promedios = [estadisticas['Promedio'] for estadisticas in estadisticas_por_producto.values()]
minimos = [estadisticas['Minimo'] for estadisticas in estadisticas_por_producto.values()]
maximos = [estadisticas['Maximo'] for estadisticas in estadisticas_por_producto.values()]
desviaciones = [estadisticas['DesviacionEstandar'] for estadisticas in estadisticas_por_producto.values()]
medianas = [estadisticas['Mediana'] for estadisticas in estadisticas_por_producto.values()]

# Obtener los índices de ordenamiento de los productos por valor máximo
indices_ordenados = sorted(range(len(maximos)), key=lambda i: maximos[i], reverse=True)

# Reorganizar las listas de productos y estadísticas según los índices de ordenamiento
productos = [productos[i] for i in indices_ordenados]
promedios = [promedios[i] for i in indices_ordenados]
minimos = [minimos[i] for i in indices_ordenados]
maximos = [maximos[i] for i in indices_ordenados]
desviaciones = [desviaciones[i] for i in indices_ordenados]
medianas = [medianas[i] for i in indices_ordenados]

# Crear una figura con 2 filas y 2 columnas para los subplots
fig, axs = plt.subplots(2, 2, figsize=(12, 10))

# Gráfico de barras para el promedio de ventas por producto (ordenado)
axs[0, 0].bar(productos, promedios, color='skyblue')
axs[0, 0].set_xlabel('Productos')
axs[0, 0].set_ylabel('Promedio de Ventas')
axs[0, 0].set_title('Promedio de Ventas por Producto (Ordenado)')

# Gráfico de líneas para el rango de ventas por producto (mínimo y máximo) (ordenado)
axs[0, 1].plot(productos, maximos, marker='o', color='lightcoral', label='Máximo')
axs[0, 1].plot(productos, minimos, marker='o', color='lightgreen', label='Mínimo')
axs[0, 1].set_xlabel('Productos')
axs[0, 1].set_ylabel('Ventas')
axs[0, 1].set_title('Rango de Ventas por Producto (Ordenado)')
axs[0, 1].legend()

# Gráfico de líneas para la desviación estándar de ventas por producto (ordenado)
axs[1, 0].plot(productos, desviaciones, marker='o', color='orange')
axs[1, 0].set_xlabel('Productos')
axs[1, 0].set_ylabel('Desviación Estándar de Ventas')
axs[1, 0].set_title('Desviación Estándar de Ventas por Producto (Ordenado)')

# Gráfico de líneas para la mediana de ventas por producto (ordenado)
axs[1, 1].plot(productos, medianas, marker='o', color='purple')
axs[1, 1].set_xlabel('Productos')
axs[1, 1].set_ylabel('Mediana de Ventas')
axs[1, 1].set_title('Mediana de Ventas por Producto (Ordenado)')

# Rotar las etiquetas del eje x para que sean legibles
plt.xticks(rotation=45)

# Ajustar el espacio entre los subplots
plt.tight_layout()

# Mostrar la figura con los subplots
plt.show()
