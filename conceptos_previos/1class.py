import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


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

#ACCESO A LOS ELEMENTOS DE UN OBJETO SERIES
#cada elemento de objeto series tiene un identificador unico 
s=  pd.Series([2,4,6,8],index=["num1","num2","num3","num4"])
print(s)
#accediendo al tercer objeto del objeto
print(s["num3"])
#aceder por la posicion
print(s.iloc[2])
print(s.loc["num3"])
#acceder al segundo y tercer elemento por posicion
print(s.iloc[2:4])

#operaciones   aritmeticas con series
#sumar
print(f"suma {np.sum(s)}")
# creacion de objetos series denominados temperaturas
temperatura = pd.Series([4.4,5.1,6.1,6.2,6.1,6.1,5.2,4.7,4.1,3.9])
s= pd.Series(temperatura,name= "temperaturas")
print(s)
s.plot()
plt.show()

#Creación de un objeto DataFrame
personas={
    "peso":pd.Series([90,80,70,60],["Santiago","Marcelo","Luis","Alejandra"]),
    "altura":pd.Series({"Santiago":180,"Marcelo":172,"Luis":174,"Alejandra":160}),
    "hijos":pd.Series([2,3],["Luis","Marcelo"])
}
df =pd.DataFrame(personas)
print(df)
df2=pd.DataFrame(
    personas,
    columns=["altura","peso"],
    index=["Santiago","Luis","Marcelo"]
)
print(df2)
#Acceso a los elementos
print(df["peso"])
#combinar metodos
df3=(df["peso"]>=60) & (df["peso"]<80)
print(df3)

print(df.iloc[1:3])
#consultas avanzadas
df4=df.query("altura >= 170 and peso >70")
print(df4)
#copiar un dataframe
df_copy =df.copy()
#añadir una nueva columna
df_copy["Cumpleaños"]=[1990,1978,1980,1994]
print(df_copy)
#añadir una columna calculada
df_copy["años"]=2025 - df_copy["Cumpleaños"]
print(df_copy)