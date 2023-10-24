import json
import matplotlib.pyplot as plt

with open('estadisticas_mes.json', 'r') as f:
    estadisticas_mes = json.load(f)

meses = list(estadisticas_mes.keys())
promedios = [estadisticas['Promedio'] for estadisticas in estadisticas_mes.values()]
minimos = [estadisticas['Minimo'] for estadisticas in estadisticas_mes.values()]
maximos = [estadisticas['Maximo'] for estadisticas in estadisticas_mes.values()]
desviaciones = [estadisticas['DesviacionEstandar'] for estadisticas in estadisticas_mes.values()]
medianas = [estadisticas['Mediana'] for estadisticas in estadisticas_mes.values()]

fig, axs = plt.subplots(2, 2, figsize=(12, 10))

# Promedio de Nacimientos por mes
axs[0, 0].bar(meses, promedios, color='skyblue')
axs[0, 0].set_xlabel('Meses')
axs[0, 0].set_ylabel('Promedio de Nacimientos')
axs[0, 0].set_title('Promedio de Nacimientos por Mes')

# Rango de Nacimientos por mes (mínimo y máximo)
axs[0, 1].plot(meses, maximos, marker='o', color='lightcoral', label='Máximo')
axs[0, 1].plot(meses, minimos, marker='o', color='lightgreen', label='Mínimo')
axs[0, 1].set_xlabel('Meses')
axs[0, 1].set_ylabel('Nacimientos')
axs[0, 1].set_title('Rango de Nacimientos por Mes')
axs[0, 1].legend()

# Desviación estándar de Nacimientos por mes
axs[1, 0].plot(meses, desviaciones, marker='o', color='green')
axs[1, 0].set_xlabel('Meses')
axs[1, 0].set_ylabel('Desviación Estándar de Nacimientos')
axs[1, 0].set_title('Desviación Estándar de Nacimientos por Mes')

# Mediana de Nacimientos por mes
axs[1, 1].plot(meses, medianas, marker='o', color='purple')
axs[1, 1].set_xlabel('Meses')
axs[1, 1].set_ylabel('Mediana de Nacimientos')
axs[1, 1].set_title('Mediana de Nacimientos por Mes')

plt.tight_layout()

plt.show()
