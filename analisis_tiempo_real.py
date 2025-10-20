from transformers import pipeline

clasificador = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")

print("Análisis de sentimientos en tiempo real (escribe 'salir' para terminar)\n")

while True:
    texto = input("Frase: ")
    if texto.lower() == "salir":
        break
    resultado = clasificador(texto)[0]
    label = resultado['label']
    stars = int(label[0])

    if stars <= 2:
        sentimiento = "Negativa"
    elif stars == 3:
        sentimiento = "Neutra"
    else:
        sentimiento = "Positiva"

    print(f"→ {sentimiento} ({label}, score: {resultado['score']:.2f})\n")
