#ciclo for
lista=[1,2,3,4]

nueva_lista=[]

for elemento in lista:
    print(elemento)
    nueva_lista.append(elemento)
print(nueva_lista)


#Acceder a un diccionario
diccionario={"clave1":"valor2", "clave2":"valor2"}

for n in diccionario:
    print(n)
    print(diccionario[n])

#Acceder a una tupla
lista=[(1,2),(3,4)]
print(lista)
for n, n2 in lista:
    print(n)
    print(n2)