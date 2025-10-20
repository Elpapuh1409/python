from transformers import pipeline

clasificador = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")

ruta = "frases.txt"

with open(ruta, "r", encoding="utf-8") as archivo:
    frases = [linea.strip() for linea in archivo if linea.strip()]

print("Análisis de frases desde archivo:\n")

for frase in frases:
    resultado = clasificador(frase)[0]
    estrellas = int(resultado['label'][0])

    if estrellas <= 2:
        sentimiento = "Negativa"
    elif estrellas == 3:
        sentimiento = "Neutra"
    else:
        sentimiento = "Positiva"

    print(f"Frase: {frase}")
    print(f"→ {sentimiento} ({resultado['label']}, score: {resultado['score']:.2f})\n")
