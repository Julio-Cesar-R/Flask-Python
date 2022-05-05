from api import basededatos,Persona
eliminar=Persona.query.get(3)
basededatos.session.delete(eliminar)
basededatos.session.commit()
print(f"Persona eliminada {eliminar}")


busqueda= Persona.query.all()
print(busqueda)

