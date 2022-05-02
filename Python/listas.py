lista=[1,2,3,"Juan",[1,9,8,7] ]
print(type(lista))
print(lista)
print(lista[-1][0])

print(lista[1:3])
lista2=["Kai","Fox"]
lista.append(lista2)#Agrega una lista dentro de una lista
print (lista)
lista3=["Xof","Kaii"]
lista.extend(lista3)# extend sirve para agregar una lista solo como elementos
print(lista)