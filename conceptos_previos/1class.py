import pandas as pd

# creacion de objetos serie 
s= pd.Series ([2,4,6,8,10]) #propiedad de pandas llamada series referente a list
print(s) 

# creacion de un objeto serie inicializando con un diccionario de python
altura = {"santiago": 180,"marcelo": 172,"luis": 174,"alejandra": 163,"Andrés":184}
s = pd.Series(altura)
print(s)
"""CREACION DE UN OBJETO SERIES INICIALIZANDOLO CON ALGUNOS DE LOS ELEMENTOS 
DE UN DICCIONARIO DE PYTHON
"""
altura = {"santiago": 180,"marcelo": 172,"luis": 174,"alejandra": 163,"Andrés":184}
s = pd.Series(altura,index=["marcelo","luis"])
print(s)

#creacion de un objeto series inicializandolo con un escalar
s=pd.Series(34,["test1","test2","test3"])
print(s)