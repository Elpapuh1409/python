from transformers import pipeline

clasificador = pipeline("sentiment-analysis", model="finiteautomata/beto-sentiment-analysis")

resultado = clasificador 
#("Soy un burro")
#Negativa
#("El arte de vencer se aprende en las derrotas.")
#Neutral
#("El éxito no es un accidente. Es trabajo duro, perseverancia, aprendizaje, sacrificio y lo más importante, amor por lo que haces o estás aprendiendo a hacer.")
#Positiva
#("Cuanto más difícil es la victoria, mayor es la felicidad de ganar.")
#Positiva
#("Si tienes miedo a fallar, probablemente falles.")
#Neutral
#("He fallado más de 9000 tiros en mi carrera. He perdido casi 300 partidos. 26 veces me han confiado el tiro ganador y lo he fallado. He fracasado una y otra vez en mi vida y es por eso que he tenido éxito.")
#Neutral

print(resultado)
