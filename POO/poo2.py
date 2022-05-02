class Persona():
    def __init__(self,nombre,apellido):
        self.nombre=nombre
        self.apellido=apellido


def cadena(obj):
    nombre=obj.nombre
    apellido=obj.apellido

    return f"tu nombre es {nombre} y tu apellido es {apellido}"


objeto=Persona("Julio","Rosas")
print(objeto.nombre)
print(objeto.apellido)
print(type(objeto))

res=cadena(objeto)
print(res)


