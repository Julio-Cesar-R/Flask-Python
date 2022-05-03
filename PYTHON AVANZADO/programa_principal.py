#programa principal
#Sirve para identificar desde que fichero se esta ejecutando una funcion
print("Estamos en el fichero programa_principal.py")

def saludo():
    print("funcion programa_principal.py")

if __name__=="__main__":
    print("Este codigo se esta ejecutando desde el programa principal")
else:
    print("Este codigo se esta ejecutando desde un fichero externo ")