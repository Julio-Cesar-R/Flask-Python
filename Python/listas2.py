lista=[1,2,3,"Kaiser"]
print(lista)
#Eliminar un elemto de lista
lista.pop()
print(lista)
lista.pop(0)
print(lista)

#Invertir la lista
lista2=[1,2,3,"Kaiser"]
lista2.reverse()
print(lista2)
#Ordenar una lista
lista3=[3,44,2,87,999,0]
lista3.sort()
print(lista3)
lista4=["a","t","b"]
lista4.sort()
print(lista4)

lista5=[1,2,3,4,["verde","rojo"]]
print(lista5[4][1])

#Lista de compresion
lista6=[[1,2,3],[4,5,6],[7,8,9]]
listanueva=[elemento[0] for elemento in lista6]
print(listanueva)
