#Tratamiento de errores
#Abrir y escribir un archivo
from typing import final


fichero=open("datos.txt","w")
fichero.write("Esta es la informacion que ira dentro del archivo")
fichero.close()

#Verificar si el archivo existe
try:
    fichero=open("datos.txt","r") #Validacion
    
except IOError:
    print("El fichero no existe error IO")#En caso de fallar
except:
    print("Error General")
else:
    print("Tratamiento de datos correcto")# En caso de que no hay error
    
finally:
    print("Tratamiento de fichero finalizado")#Este codigo se muestra sin importar el resultado de la prueba

print("Continua el programa")


print(fichero.read())
fichero.close()
