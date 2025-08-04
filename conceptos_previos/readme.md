"mark down -  sirve para dar informacion al usuario" 
# comandos 
```
pip list 
python --version / Python 3.13.0
git --version
https://git-scm.com
```
## crear entorno virtual
python -m venv env
-- es obligatorio hasta venv, despues de ahi es solo el nombre 
## activar entorno
env\scripts\activate
sino se activa el ejecutor, se ejecuta poweshell y se coloca: set-ExecutionPolicy Unrestricted
y escriba s 
## Estructura de datos en Pandas 
| tipo      | definicion                                    |
| --------- | --------------------------------------------- |
| Series    | Array de una dimensión                        |
| DataFrame | se corresponde con una tabla de 2 dimensiones |
| panel     | similar a un diccionario de DataFrame         |

alt + shif + f para formatear datos
## creacion de objetos series
```
import pandas as pd #pip install pandas
# creacion de objetos serie 
s= pd.Series ([2,4,6,8,10])
print(s)

``` 
## manejo de git
>git init #inicia el repositorio
git add 
git commit -m "introducción a pandas 5%"
    git config --global user.email "you@example.com"
    git config --global user.name "Your Name"
usergithub: andro312 
correo: andaesra312@gmail.com
contra: elbot_andro312

crear archivo requeriment
pip  freeze  > requirements.txt # con el env activo para que muestre cuales son las librerias activas