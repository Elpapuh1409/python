from transformers import pipeline

# Cargar modelo de sentimiento multilabel (ajustado a español o multilingüe)
clasificador = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")

# Lista de frases deportivas (puedes reemplazar por las que quieras)
frases = [
    "Qué golazo impresionante, esto es fútbol del bueno.",
    "El árbitro arruinó el partido, fue un desastre.",
    "El equipo jugó con calma, sin emociones fuertes.",
    "La afición está feliz por el resultado.",
    "Hoy no fue su mejor día, se notó la falta de energía."
]

# Clasificar todas de una vez
resultados = clasificador(frases)

# Mostrar resultados individuales
for frase, resultado in zip(frases, resultados):
    print(f"Frase: {frase}")
    print(f"Resultado: {resultado}\n")

# Contar positivas, negativas, neutras (según estrellas del modelo 1-5)
pos, neg, neu = 0, 0, 0
for r in resultados:
    label = r['label']
    stars = int(label[0])  # el modelo da "1 star" a "5 stars"
    if stars <= 2:
        neg += 1
    elif stars == 3:
        neu += 1
    else:
        pos += 1

print("Resumen:")
print(f"Positivas: {pos}")
print(f"Neutras: {neu}")
print(f"Negativas: {neg}")
