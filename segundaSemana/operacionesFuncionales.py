# filter(funcion,secuencia)
from functools import reduce


es_par = lambda numero : numero %2 == 0
numeros = [1,2,3,4,5,6,7,8,9,10,11]
pares = list(filter(es_par,numeros))
print(pares)

# map(funcion,secuencia)
cuadrado = lambda numero : numero **2
cuadrados = list(map(cuadrado,numeros))
print(cuadrados)

#reduce(funcion,secuencia)
suma = lambda numero1, numero2 : numero1 + numero2
total = reduce(suma, numeros)
print(total)