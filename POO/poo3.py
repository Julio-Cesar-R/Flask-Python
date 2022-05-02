#Poo
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

