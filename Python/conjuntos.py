#Conjuntos con py
#No se pueden repetir valores
from numpy import conj


conjunto=set()
print(type(conjunto))

for n in range(1,33,2):

    conjunto.add(n)

conjunto.add ("kaiser")
print(conjunto) #Muestra el conjunto ordenado

conjunto.discard("kaiser")
conjunto.discard(1)
print(conjunto)

#Eliminar valores repetidos de una lista
lista=[1,1,2,2,2,2,2,2,2,2]
conju=set(lista)
print (conju)