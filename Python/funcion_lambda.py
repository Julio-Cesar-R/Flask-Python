#Funciones lambda (funciones anonimas (calculo interno dentro de otra funcion))

lista=[1,2,3,4,5,6]
def par(numero):
    if numero %2==0:
        return f"Numero {numero} es par"
    else:
        return f"Numero {numero} es impar"
for n in lista:
    res=par(n)
    print(res)

#Funciones lambda
'''def pares(numero):
    resultado=(numero%2)==0
    return resultado
'''
filtro=filter(lambda numero:numero%2==0,lista) #compara una lista con una funcion lambda
print(type(filtro))
pares=list(filtro)
print(pares)
