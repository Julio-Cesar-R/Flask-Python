#----------------------LIBRERIAS----------------------------
from flask import Flask
from flask_restful  import Resource,Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
#app
app=Flask(__name__)
api=Api(app)
#---------------------CONEXION-------------------------
directorio=os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(directorio,'personas.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

basededatos=SQLAlchemy(app)
Migrate(app,basededatos)
#---------------BASE DE DATOS MODELO---------------------
class PersonaDB(basededatos.Model):
    id = basededatos.Column(basededatos.Integer, primary_key=True)
    nombre = basededatos.Column(basededatos.String(100))
    apellido = basededatos.Column(basededatos.String(100))
    direccion = basededatos.Column(basededatos.String(100))
    def __init__ (self,nombre,apellido,direccion):
        self.nombre = nombre
        self.apellido=apellido
        self.direccion=direccion
    def json(self):
        return {"id":self.id , "nombre": self.nombre,"apellido":self.apellido,"direccion":self.direccion}

#------------------------------------------------------------

#----------------RUTAS------------------------------
class Personas(Resource):
    #GET
    def get(self,valor):
        persona=PersonaDB.query.filter_by(id=valor).first()
        if persona:
            return persona.json()
        return {"resultado":"Persona no existe en la base de datos"}

    #POST

    def post (self,valor,valor2,valor3):
        print(valor)
        print(valor2)
        print(valor3)
        persona=PersonaDB(nombre=valor,apellido=valor2,direccion=valor3)
        basededatos.session.add(persona)
        basededatos.session.commit()
        return {"respuesta":"Nombre añadido a la base de datos"}
    #DELETE
    def delete(self,valor):
        persona=PersonaDB.query.filter_by(id=valor).first()
        basededatos.session.delete(persona)
        basededatos.session.commit()
        return {"resultado":"Persona borrada correctamente"}

#BUSCAR LISTA COMPLETA

class Lista(Resource):
    def get(self):
        personas=PersonaDB.query.all()
        lista_personas=[persona.json()for persona in personas]
        return {"resultado":lista_personas}

#Cantidad de parametros que recibe la appi (cadaa ruta utiliza cuantos sean necesarios)
api.add_resource(Personas,"/personas/<string:valor>,<string:valor2>,<string:valor3>")
api.add_resource(Lista,"/lista")

#---------------------------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True)