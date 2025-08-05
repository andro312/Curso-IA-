import pandas as pd

# creacion de objetos serie 
s= pd.Series ([2,4,6,8,10]) #propiedad de pandas llamada series referente a list
print(s) 

# creacion de un objeto serie inicializando con un diccionario de python
altura = {"santiago": 180,"marcelo": 172,"luis": 174,"alejandra": 163,"Andrés":184}
s = pd.Series(altura)
print(s)
