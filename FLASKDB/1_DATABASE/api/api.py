#                    CONFIGURACION DE LA BASE DE DATOS
#---------------------------------------------------------------------------------------

#Rutas
from email.mime import base
import os

#Migracion de datos
from flask_migrate import Migrate

#Apis
from flask import Flask
#Conexion DB
from flask_sqlalchemy import SQLAlchemy

#ruta actual

ruta_actual=os.path.abspath(os.path.dirname(__file__))
print(ruta_actual)


#Api con base de datos
app=Flask("__name__",template_folder="../template")
#Ruta de la base de datos (configuraciones)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///"+ os.path.join(ruta_actual,"datos.sqlite")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False

#Base de datos se iguala a las configuraciones de la app
basededatos=SQLAlchemy(app)
#---------------------------------------------------------------------------------------------------------
#                           MODELO DE LA BASE DE DATOS

#Clase que hereda la base de datos
class Persona (basededatos.Model):  
    #Nombre de la tabla
    __tablename__="Personas"
    #Campos
    id=basededatos.Column(basededatos.Integer,primary_key=True)#Primary Key
    nombre=basededatos.Column(basededatos.Text)
    edad=basededatos.Column(basededatos.Integer)
    color=basededatos.Column(basededatos.Text)
    trabajo=basededatos.Column(basededatos.Text)

    #Constructor de la clase
    def __init__(self,nombre,edad,color ,trabajo):
        self.nombre=nombre
        self.edad=edad
        self.color=color
        self.trabajo=trabajo
    #Representacion ( es como la funcion str)
    def __repr__(self):
        text=f"Personas: nombre={self.nombre} edad={self.edad} color:{self.color} trabajo:{self.trabajo} "
        return text

#------------------------MIGRACION DE DATOS--------------------------------
#Migracion de datos
Migrate(app,basededatos)

#1-Nos movemos al directorio donde estan los ficheros(terminal de comandos de preferencia power shell de windows)
#PS C:\Users\julio\OneDrive\Documentos\Cesar\Python y Flask, desarrollo web y apis tipo rest\flaskdb\1_database\api> 
    #Para mac y linux "export FLASK_APP=api.py
    # Para windows "set FLASK_APP=api.py"
#2-Pasar el modelo modificado a la base de datos
    #"flask db init"
#3 hacer la migracion
    # "flask db migrate -m "Cambios de estructura" ""
#4-actualizar
    # "flask db upgrade"