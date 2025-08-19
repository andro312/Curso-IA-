from transformers import pipeline
#crear un pipeline de analisis de sentimientos
clasificador=pipeline('sentiment-analysis')
#analisar una sentencia
resultado=clasificador("te amo")
print(resultado)

resultado2=clasificador("no me gusta estudiar el sabado")
print(resultado2)