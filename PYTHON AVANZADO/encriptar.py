#----------------------ENCRIPTAR--------------------------
#Instalar librerias pip install Bcrypt-Flask y pip install werkzeug
#Libreria para encriptar cadenas de caracteres
from modulefinder import IMPORT_NAME
from flask_bcrypt import Bcrypt

#Instacia de la clase
generador=Bcrypt()
#Texto a encriptar
passw="kaiserfox"
#Genera la encriptacion
pass_encriptada=generador.generate_password_hash(passw)
#Verificar coincidencias
intento_pass="kai"
verificar=generador.check_password_hash(pass_encriptada,intento_pass)
#--------------------------------------------------------------------------
#---------------------------OTRA OPCION------------------------------------
#Libreria
from werkzeug.security import generate_password_hash, check_password_hash
#Contraseña
password="kaiserfox"
#encriptar contraseña
password_encriptada=generate_password_hash(password)
print(password_encriptada)

#Verificar coincidencias
intento_password="kaiserfo"
password_validacion= check_password_hash(password_encriptada,intento_password)
print(password_validacion)
