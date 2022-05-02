#Funciones decoradoras, una funcion que se apllica sobre potra funcion

def asteriscos(funcion):#Funcion decoradora
    def poner_asteriscos():
        print("*****************************")
        funcion()#Funcion externa
        print("*****************************")

    return poner_asteriscos

def imprimir():
    print("Buenos dias")

#Reasignamos la funcion para que pase por la funcion decoradora
imprimir=asteriscos(imprimir) 
imprimir()


#Otra forma

def asteriscos1(funcion):#Funcion decoradora
    def poner_asteriscos():
        print("*****************************")
        funcion()#Funcion externa
        print("*****************************")

    return poner_asteriscos

@asteriscos
def imprimir():
    print("Buenos dias")

imprimir()

