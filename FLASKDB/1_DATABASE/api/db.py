#-------------------EJECUTAR LA BASE DE DATOS EN CONSOLA-------------
#MIGRAR BASE DE DATOS
#Importar la clase migrate en api.py




#--------------------PRUEBAS DE LA BASE DE DATOS-----------------------
#Se importa la base de datos y la clase Persona(Modelo de la base)
from api import basededatos,Persona

#Crea la base de datos mediante el modelo
basededatos.create_all()

#Se crea una instancia y se le mandan datos a la tabla
#La primary key es autoincremental
persona1=Persona("Kaiser",30,"Azul")
persona2=Persona("Fox",29,"Rojo")
persona3=Persona("Maria",20,"Verde")

#Insert
basededatos.session.add_all([persona1,persona2,persona3])
#Guarda los cambios en la base
basededatos.session.commit()

#Consultar todos los registros
personas=Persona.query.all()
print(personas)

#Buscar por filto
bus_per=Persona.query.filter_by(nombre="Fox")
print("Filtro por nombre Fox")
print(bus_per.all())
#Buscar por id
bus_id=Persona.query.get(1)
print("Filtro por id")
print(bus_id)

#Actualizar registro
act_per=Persona.query.get(1)
act_per.edad=66
basededatos.session.add(act_per)
basededatos.session.commit()

#Eliminar
eliminar=Persona.query.get(3)
basededatos.session.delete(eliminar)
basededatos.session.commit()
print(f"Persona eliminada {eliminar}")

all_personas=Persona.query.all()
print(all_personas)