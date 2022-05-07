#---------APLICACION FLASK, CLAVE SECRETA, CONEXION A LA BASE-----------------
#--------------------LIBRERIAS-------------------------------
#Ruta de la base
import os
#Rutas
from flask import Flask
#Conexion a la base
from flask_sqlalchemy import SQLAlchemy
#Migracion de datos
from flask_migrate import Migrate
#Admin del login
from flask_login import LoginManager
#-------------------------------------------------------------------

#Instancias a Loginmanager
gestor = LoginManager()

#App
app = Flask("__name__",template_folder="../template")
#Clave secreta
app.config['SECRET_KEY'] = 'clavesecreta'
#Crear ruta
directorio = os.path.abspath(os.path.dirname(__file__))
#db configuraciones
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(directorio,'loginbd.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Variable de la base de datos
basededatos = SQLAlchemy(app)
#Migracion
Migrate(app,basededatos)
#Login manager
gestor.init_app(app,)
gestor.login_view = 'login'
