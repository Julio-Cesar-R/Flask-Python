#programa principal
import programa_principal as py
print("Estamos en el fichero programa_principal2.py")


if __name__=="__main__":
    print("Este codigo se esta ejecutando desde el programa principal2")
else:
    print("Este codigo se esta ejecutando desde un fichero externo ")

py.saludo()