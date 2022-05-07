#------------------MODELO DE LA BASE ------------------------------------
#-------------------------Librerias-------------------------------
#Importar la base y el gestor del login
from conexion import basededatos,gestor #importa desde la carpeta que contiene los archivos.py
#Encriptacion
from werkzeug.security import generate_password_hash, check_password_hash
#Login maneger
from flask_login import UserMixin

#Funcion que carga al usuario si ya esta logeado
@gestor.user_loader
def load_user(Usuario_id):
    return Usuario.query.get(Usuario_id)
#-----------------------------------------------------------------------
#---------------------------------TABLAS-------------------------------


class Usuario(basededatos.Model, UserMixin):
    __tablename__ = 'usuarios'
    #Campos de la tabla
    id = basededatos.Column(basededatos.Integer, primary_key=True)
    email = basededatos.Column(basededatos.String(64), unique=True, index=True)
    nombre = basededatos.Column(basededatos.String(64), unique=True, index=True)
    password_encriptada = basededatos.Column(basededatos.String(128))
    #Constructor
    def __init__(self,email,nombre,password):
        self.email = email
        self.nombre = nombre
        #Encriptamos
        self.password_encriptada = generate_password_hash(password)
    #Funcion que verifica la password
    def verificar_password(self,password):
        return check_password_hash(self.password_encriptada,password)
