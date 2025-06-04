# Parcial-paradigmas.
Parcial paradigmas. 
Nicolas Sanchez Calderon-1019843707.

Por medio del presente github hare entrega del parcial #3 de paradigmas de programacion.

La primera funcion usa un enfoque iterativo con un ciclo que recorre los armonicos, y la segunda usa recursion para calcular los coeficientes. Ambas funciones devuelven los resultados, pero no imprimen nada por si solas, esto lo hice asi porque entendi el parcial lo pide de esa forma que las funciones deben ser llamadas desde otro archivo para poder comparar sus resultados.

Toda la comparacion se hace en un archivo aparte (comparacion.py), donde se define la funcion f(t), se llaman ambas implementaciones con diferentes valores de N (5, 10, 20 y 50), y se mide el tiempo que tarda cada una. no quise graficar ya que esto era opcional y asi no sobrecomplicaba el codigo; Decidi hacer una tablita en la salida.


Procedere a pegar la tabla trasncrita a markdown para que desde el README sea mas sencillo entender el resultado:
| N  | Iterativo | Recursivo |
| -- | --------- | --------- |
| 5  | 0.000158  | 0.000137  |
| 10 | 0.000241  | 0.000244  |
| 20 | 0.000463  | 0.000474  |
| 50 | 0.001142  | 0.001166  |

se puede ver que los tiempos de ejecucion son similares cuando N es bajo, pero a medida que aumenta el numero de armonicos el metodo iterativo empieza a ser un poco mas rapido que el recursivo. Aunque la diferencia es mas ben poca pues se trata de mili segundos, el enfoque iterativo es un poco mas eficiente y practico, especialmente si se quiere usar con valores de N mas grandes.






