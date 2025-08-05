import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Dataset ficticio
datos_estudiantes = {
    "peso": pd.Series([55, 68, 74, 60, 72], index=["Ana", "Carlos", "Daniela", "Eduardo", "Fernanda"]),
    "altura": pd.Series([162, 175, 168, 180, 170], index=["Ana", "Carlos", "Daniela", "Eduardo", "Fernanda"]),
    "promedio": pd.Series([4.5, 3.8, 4.2, 2.9, 3.5], index=["Ana", "Carlos", "Daniela", "Eduardo", "Fernanda"]),
    "edad": pd.Series([17, 18, 17, 19, 18], index=["Ana", "Carlos", "Daniela", "Eduardo", "Fernanda"])
}

df = pd.DataFrame(datos_estudiantes)
print(df)

#crear una serie con los nombres y alturas de los estudiantes
altur = pd.DataFrame(datos_estudiantes,columns=["altura"],index=["Ana", "Carlos", "Daniela", "Eduardo", "Fernanda"])
print(altur)
#cual es la altura de daniela?
#usando loc
print(f"la altura de daniela es de:{altur.loc["Daniela"]['altura']}")
#usando iloc
print(f"la altura de daniela es de:{altur.iloc[2]['altura']}")
#Accede al promedio de calificación de Carlos de 3 formas diferentes
promedios= pd.DataFrame(df,columns=["promedio"],index=["Carlos"])
print(f"el promedio de carlos es:{promedios.loc["Carlos"]["promedio"]}")
#Filtra a los estudiantes con promedio mayor o igual a 4.0
df2=df.query("promedio >= 4.0")
print(df2)
dfcopy= df.copy()
dfcopy["mayoredad"]= ["no","si","no","si","si"]
print(dfcopy)
dfcopy["añonacer"]= 2025 - dfcopy["edad"]
print(dfcopy)
promedios2= df["promedio"]
print(promedios2)
promedios2.plot()
plt.show()
del dfcopy["peso"]
print(dfcopy)
dtf3 = pd.DataFrame(dfcopy, columns=["edad","añonacer"],
                    index=["Ana", "Carlos", "Daniela", "Eduardo", "Fernanda"])
print(dtf3)