# Trabajo con linux en windos
en administrador command promt 
```
wsl --install

```
| libreria     | comando                 |
| ------------ | ----------------------- |
| transformers | pip install transfomers |
| torch        | pip install torch       |

## codigo de ejemplo 1 
```
from transformers import pipeline
#crear un pipeline de analisis de sentimientos
clasificador=pipeline('sentiment-analysis')
#analisar una sentencia
resultado=clasificador("Me encanta usar la libreria transformers")
print(resultado)
resultado2=clasificador("no me gusta estudiar el sabado")
print(resultado2)

```