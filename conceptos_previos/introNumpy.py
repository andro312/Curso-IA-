import numpy as np
import matplotlib.pyplot as plt

a= np.zeros((2,4))
print(a)

#imprimir las dimensiones de la matriz
print(a.shape) 
#imprimir numero de dimensiones
print("numero de dimensiones:",a.ndim)
#imprimir el tamaño de una matriz
print("tamaño:",a.size)
"""
array o matriz cuyos valores son todos el valor indicado como
segun parametro de la funcion
"""
c=np.full((2,3,4),8)
#print(c)
"""
Inicializa los valores del array con lo que haya en memoria en el momento
el llenado del empty es aleatorio 
"""
d=np.empty((2,3,4))
#print(d)
#Inicializacion del array usando uno de python
f= np.array([[1,2,3],[4,5,6]])
#print(f)

"""
creacion del array utilizando una funcion basada en rangos
(minimo, maximo, numero de elementos con valores aleatorios)
"""
#print(np.linspace(0,6,10))
"""
inicializacion de un array con valores aleatorios
"""
e=np.random.rand(2,3,4)
#print(e)
"""
inicializacion del array con valores aleatorios conforme a una distribucion normal
"""
g= np.random.rand(2,4)
#print(g)

"""
Histograma con valores aleatorios
"""
h=np.random.rand(100)

#plt.hist(h)
#plt.show()

i= np.array([1,2,3,2,2,2,4,5,6,7,8])
#plt.hist(i,bins=15)
#plt.show()
def func(x,y):
    return x+2*y

i=np.fromfunction(func,(3,5))
print(i)
