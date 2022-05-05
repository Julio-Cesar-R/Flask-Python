#Importamos las tablas y la base

from modelo import basededatos,Mascota,Juguete,Propietario

mascotas1=Mascota.query.filter_by(nombre="Lucy").first()
print(mascotas1)
mascotas1.mostrar_juguetes()



#Inserta mascotas
mascota1=Mascota("Mia")
mascota2=Mascota("Lucy")
basededatos.session.add_all([mascota1,mascota2])
basededatos.session.commit()
#Muestra todos los resultados
mascotas=Mascota.query.all()
print (mascotas)
#Busqueda por filtro
mas_filt=Mascota.query.filter_by(nombre="Lucy").first()
#Propietario
propietario1=Propietario("Kaiser",mas_filt.id)
#-------------------
basededatos.session.add(propietario1)
basededatos.session.commit()

#Insertar juguetes
juguete1=Juguete("Pelota",mas_filt.id)
juguete2=Juguete("Peluche",mas_filt.id)

basededatos.session.add_all([juguete1,juguete2])
basededatos.session.commit()

#Mostrar juguetes de una mascota
mascotas1=Mascota.query.filter_by(nombre="Lucy").first()
print(mascotas1)
mascotas1.mostrar_juguetes()