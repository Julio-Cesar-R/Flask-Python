#Variables locales y globales
numero=30 #Variables globales
texto="Hola"

def funcion1():
    numero2=35#La variable es local en esta funcion
    print(numero2)
    salud="Hola mundo"
    print(salud)
    print(locals())#Muestra las variables locales de esta funcion

print(numero)
funcion1()
#Imprimir todas la variables globales
print(globals())
print(globals()["__file__"])

