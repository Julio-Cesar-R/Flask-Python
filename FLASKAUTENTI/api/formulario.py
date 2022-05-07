#-------------------------FORMULARIOS-------------------------------
#-------------------------LIBRERIAS---------------------------------
#Flask form
from flask_wtf import FlaskForm
#Campos Flask form
from wtforms import StringField, PasswordField, SubmitField
#Valida campos
from wtforms.validators import DataRequired, Email, EqualTo
#Errores
from wtforms import ValidationError

#Importar modelo usuario
from modelos import Usuario
#-------------------------------------------------------------

#------------------------FORMULARIOS--------------------------------
#Formulario registrar
class Formulario_Registro(FlaskForm):
    #Campos y validadores
    email = StringField('Email',validators=[DataRequired(),Email()])
    nombre = StringField('Nombre',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired(),EqualTo('password_repetir',message="Las password no coinciden")])
    password_repetir = PasswordField('Repetir password',validators=[DataRequired()])
    boton = SubmitField('Registrar')

    #Verificar que el email no exista
    def verificar_mail(self,parametro):
        if Usuario.query.filter_by(email=parametro.data).first():
            raise ValidationError('Error. Este mail ya ha sido utilizado')
    #verificar que el nombre de usuario no se repita
    def verificar_nombre(self,parametro):
        if Usuario.query.filter_by(nombre=parametro.data).first():
            raise ValidationError('Error. Este nombre ya ha sido utilizado')
#Formulario login
class Formulario_Login(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    boton = SubmitField('Entrar')
#---------------------------------------------------------------------------------------------------------
