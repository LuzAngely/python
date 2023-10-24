import json
import matplotlib.pyplot as plt

with open('estadisticas_sexo.json', 'r') as f:
    estadisticas_sexo = json.load(f)

sexos = list(estadisticas_sexo.keys())
promedios = [estadisticas['Promedio'] for estadisticas in estadisticas_sexo.values()]
minimos = [estadisticas['Minimo'] for estadisticas in estadisticas_sexo.values()]
maximos = [estadisticas['Maximo'] for estadisticas in estadisticas_sexo.values()]
desviaciones = [estadisticas['DesviacionEstandar'] for estadisticas in estadisticas_sexo.values()]
medianas = [estadisticas['Mediana'] for estadisticas in estadisticas_sexo.values()]

indices_ordenados = sorted(range(len(maximos)), key=lambda i: maximos[i], reverse=True)

sexos = [sexos[i] for i in indices_ordenados]
promedios = [promedios[i] for i in indices_ordenados]
minimos = [minimos[i] for i in indices_ordenados]
maximos = [maximos[i] for i in indices_ordenados]
desviaciones = [desviaciones[i] for i in indices_ordenados]
medianas = [medianas[i] for i in indices_ordenados]

fig, axs = plt.subplots(2, 2, figsize=(12, 10))

# Promedio de nacimientos por sexo
axs[0, 0].bar(sexos, promedios, color='skyblue')
axs[0, 0].set_xlabel('sexos')
axs[0, 0].set_ylabel('Promedio de nacimientos')
axs[0, 0].set_title('Promedio de nacimientos por sexo')

# Rango de nacimientos por sexo
axs[0, 1].plot(sexos, maximos, marker='o', color='lightcoral', label='Máximo')
axs[0, 1].plot(sexos, minimos, marker='o', color='lightblue', label='Mínimo')
axs[0, 1].set_xlabel('sexos')
axs[0, 1].set_ylabel('nacimientos')
axs[0, 1].set_title('Rango de nacimientos por sexo')
axs[0, 1].legend()

# Desviación estándar de nacimientos por sexo
axs[1, 0].plot(sexos, desviaciones, marker='o', color='lightgreen')
axs[1, 0].set_xlabel('sexos')
axs[1, 0].set_ylabel('Desviación Estándar de nacimientos')
axs[1, 0].set_title('Desviación Estándar de nacimientos por sexo')

# Mediana de nacimientos por sexo
axs[1, 1].plot(sexos, medianas, marker='o', color='purple')
axs[1, 1].set_xlabel('sexos')
axs[1, 1].set_ylabel('Mediana de nacimientos')
axs[1, 1].set_title('Mediana de nacimientos por sexo')

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()
