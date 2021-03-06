#-----------------FORMULARIOS FLASK FORM-----------------
#Libreria Flaskform
from flask_wtf import FlaskForm
#Tipos de campos
from wtforms import StringField,IntegerField,SubmitField
#---------------------------------------------------------------------------
#------------------FORMULARIOS----------------------------------------------
class FormularioAlta(FlaskForm):
    nombre=StringField("Nombre de la mascota :")
    edad=IntegerField("Edad de la mascota :")
    sexo=StringField("Sexo de la mascota :")
    dueno=StringField("Nombre del dueño: ")
    boton=SubmitField("Añadir")

class FormularioBaja(FlaskForm):
    id=IntegerField("Identificador de la mascota")
    boton=SubmitField("Borrar")
#---------------------------------------------------------