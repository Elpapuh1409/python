import csv
import matplotlib.pyplot as plt

archivo = "resultados.csv"

positivas = 0
neutras = 0
negativas = 0

with open(archivo, "r", encoding="utf-8") as f:
    lector = csv.DictReader(f)
    for fila in lector:
        if fila["Sentimiento"] == "Positiva":
            positivas += 1
        elif fila["Sentimiento"] == "Neutra":
            neutras += 1
        elif fila["Sentimiento"] == "Negativa":
            negativas += 1

# Datos para la gráfica
categorias = ["Positivas", "Neutras", "Negativas"]
valores = [positivas, neutras, negativas]

plt.bar(categorias, valores)
plt.title("Resumen de Sentimientos")
plt.xlabel("Tipo de sentimiento")
plt.ylabel("Cantidad de frases")
plt.tight_layout()
plt.show()
