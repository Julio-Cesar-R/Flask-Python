#Poo
from telnetlib import SE


class Persona():
    texto=""
    def __init__(self,nombre,apellido):
        self.nombre=nombre
        self.apellido=apellido

    def saludar(self):
        self.texto=f"Hola mi nombre es {self.nombre}"
        return self.texto



objeto=Persona("Julio","Rosas")
print(objeto.nombre)
print(objeto.apellido)
print(type(objeto))
re=objeto.saludar()
print(re)

class Adulto(Persona):
    def __init__(self, nombre, apellido):
        Persona.__init__(self,nombre,apellido)

    def saludar(self):
        self.texto="Hola soy adulto"
        return self.texto

    def grabar_tarjeta(self,tarjeta):
        self.tarjeta=tarjeta
       
    def __str__(self) :
        self.texto= f"Nombre:{self.nombre} Apellido:{self.apellido} Tajeta: {self.tarjeta}"
        return self.texto


ob=Adulto("Kai","Fox")
print(type(ob))
texto1=ob.saludar()
print(texto1)

ob.grabar_tarjeta("nkhjkfhsdfufhwflaks")

#Funcion especial STR def __str__(self) :

print(ob)
