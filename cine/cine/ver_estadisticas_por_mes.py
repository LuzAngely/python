import json
import matplotlib.pyplot as plt

# Cargar los datos del archivo JSON
with open('estadisticas_por_mes.json', 'r') as f:
    estadisticas_por_mes = json.load(f)

# Extraer los nombres de los meses y las estadísticas
meses = list(estadisticas_por_mes.keys())
promedios = [estadisticas['Promedio'] for estadisticas in estadisticas_por_mes.values()]
minimos = [estadisticas['Minimo'] for estadisticas in estadisticas_por_mes.values()]
maximos = [estadisticas['Maximo'] for estadisticas in estadisticas_por_mes.values()]
desviaciones = [estadisticas['DesviacionEstandar'] for estadisticas in estadisticas_por_mes.values()]
medianas = [estadisticas['Mediana'] for estadisticas in estadisticas_por_mes.values()]

# Crear una figura con 2 filas y 2 columnas para los subplots
fig, axs = plt.subplots(2, 2, figsize=(12, 10))

# Gráfico de barras para el promedio de ventas por mes
axs[0, 0].bar(meses, promedios, color='skyblue')
axs[0, 0].set_xlabel('Meses')
axs[0, 0].set_ylabel('Promedio de Ventas')
axs[0, 0].set_title('Promedio de Ventas por Mes')

# Gráfico de líneas para el rango de ventas por mes (mínimo y máximo)
axs[0, 1].plot(meses, maximos, marker='o', color='lightcoral', label='Máximo')
axs[0, 1].plot(meses, minimos, marker='o', color='lightgreen', label='Mínimo')
axs[0, 1].set_xlabel('Meses')
axs[0, 1].set_ylabel('Ventas')
axs[0, 1].set_title('Rango de Ventas por Mes')
axs[0, 1].legend()

# Gráfico de líneas para la desviación estándar de ventas por mes
axs[1, 0].plot(meses, desviaciones, marker='o', color='orange')
axs[1, 0].set_xlabel('Meses')
axs[1, 0].set_ylabel('Desviación Estándar de Ventas')
axs[1, 0].set_title('Desviación Estándar de Ventas por Mes')

# Gráfico de líneas para la mediana de ventas por mes
axs[1, 1].plot(meses, medianas, marker='o', color='purple')
axs[1, 1].set_xlabel('Meses')
axs[1, 1].set_ylabel('Mediana de Ventas')
axs[1, 1].set_title('Mediana de Ventas por Mes')

# Ajustar el espacio entre los subplots
plt.tight_layout()

# Mostrar la figura con los subplots
plt.show()
