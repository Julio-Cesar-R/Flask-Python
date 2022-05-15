#----------------------LIBRERIAS----------------------------

#from crypt import methods
from flask import Flask, jsonify,request
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
    direccion = basededatos.Column(basededatos.String(100))
    

    def __init__ (self,nombre,direccion):
        self.nombre = nombre
        self.direccion=direccion
       
    def json(self):
        return {"id":self.id , "nombre": self.nombre,"direccion":self.direccion}

#------------------------------------------------------------

#----------------RUTAS------------------------------
@app.route("/cursos",methods=["GET"])
def listar_cursos():
   try:
       persona=PersonaDB.query.all()
       lista_personas=[person.json()for person in persona]
       print(lista_personas)
       return jsonify({"respuesta":lista_personas})

   except Exception as ex:
       return jsonify({"mensaje":"Error"})

@app.route("/cursos",methods=["POST"])
def agregar_cursos():
   try:
       name=request.json["nombre"]
       adrees=request.json["direccion"]
       persona=PersonaDB(nombre=name,direccion=adrees)
       basededatos.session.add(persona)
       basededatos.session.commit()
       return jsonify({"respuesta":"Curso registrado"})

   except Exception as ex:
       return jsonify({"mensaje":"Error"})




@app.route("/cursos/<codigo>",methods=["GET"])
def leer_curso(codigo):
    try:
        persona=PersonaDB.query.filter_by(id=codigo).first()
        if persona:
            return jsonify({"Respuesta":persona.json()})
        return jsonify({"resultado":"Persona no existe en la base de datos"})
    except Exception as ex:
        return jsonify({"respuesta":"Error"})


@app.route("/cursos/<codigo>",methods=["DELETE"])
def eliminar_curso(codigo):
    try:
        persona=PersonaDB.query.filter_by(id=codigo).first()
        if persona:
            basededatos.session.delete(persona)
            basededatos.session.commit()
            return jsonify({"Respuesta":"Persona eliminado"})
        return jsonify({"resultado":"Persona no existe en la base de datos"})


    except Exception as ex:
        return jsonify({"respuesta":"Error"})



@app.route("/cursos/<codigo>",methods=["PUT"])
def actualizar_curso(codigo):
    try:
        persona=PersonaDB.query.filter_by(id=codigo).first()
        if persona:
            persona.nombre=request.json["nombre"]
            persona.direccion=request.json["direccion"]
            print(persona.nombre) 
            basededatos.session.add(persona)
            basededatos.session.commit()
             
            return jsonify({"Respuesta":"Persona actualizada"})
        return jsonify({"resultado":"Persona no existe en la base de datos"})


    except Exception as ex:
        return jsonify({"respuesta":"Error"})    

def pagina_no_encontrada(error):
    return "<h1>Pagina no encontrada</h1>"


if __name__ == "__main__":
    app.register_error_handler(404,pagina_no_encontrada)
    app.run(debug=True)





#---------------------------------------------------------------------

