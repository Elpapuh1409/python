import csv
from transformers import pipeline

clasificador = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")

ruta_entrada = "frases.txt"
ruta_salida = "resultados.csv"

with open(ruta_entrada, "r", encoding="utf-8") as archivo:
    frases = [linea.strip() for linea in archivo if linea.strip()]

resultados = []

for frase in frases:
    resultado = clasificador(frase)[0]
    estrellas = int(resultado['label'][0])

    if estrellas <= 2:
        sentimiento = "Negativa"
    elif estrellas == 3:
        sentimiento = "Neutra"
    else:
        sentimiento = "Positiva"

    resultados.append([frase, sentimiento, resultado['label'], f"{resultado['score']:.2f}"])

with open(ruta_salida, "w", encoding="utf-8", newline="") as archivo_csv:
    escritor = csv.writer(archivo_csv)
    escritor.writerow(["Frase", "Sentimiento", "Label", "Score"])
    escritor.writerows(resultados)

print(f"Análisis guardado en {ruta_salida}")
