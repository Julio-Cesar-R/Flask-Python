#Flask formulario con diferentes tipos de entradas

#FLASK FORM pip install Flask_WTF

#Flask con session y redirect

#Flask y render template
from flask import Flask, render_template, session,redirect, url_for
#Clase de tipo flask form
from flask_wtf import FlaskForm
#Campos de formulario
from wtforms import (StringField,BooleanField,DateTimeField,SelectField,
                    RadioField,SearchField,TelField,TextAreaField, SubmitField) 

#Libreria para validar
from wtforms.validators import DataRequired


#Iniciamos nuestra aplicacion
app = Flask("__name__",template_folder="../template/")
#clave secreta de app
app.config['SECRET_KEY'] = 'clavesecreta'

#Formulario

class Formulario(FlaskForm):
    nombre=StringField("Nombre",validators=[DataRequired()])
    edad=BooleanField("Eres mayor de edad",validators=[DataRequired()])
    sexo=RadioField("Sexo",choices=[("h","Hombre"),("m","Mujer")] )
    color=SelectField("Color favorito",choices=[("a","Azul"),("r","Rojo"),("v","Verde")])
    comentario=TextAreaField()
    boton=SubmitField("Enviar")

#Aplicacion Flask
@app.route('/informacion')#Se puede accesar a esta ruta por estos dos metodos
def informacion():

    return render_template('informacion.html')


@app.route("/datos",methods=["GET","POST"])
def datos():
    miformulario=Formulario()
    if miformulario.validate_on_submit():
        session["nombre"]=miformulario.nombre.data
        session["edad"]=miformulario.edad.data
        session ["sexo"]=miformulario.sexo.data
        session["color"]=miformulario.color.data
        session["comentario"]=miformulario.comentario.data
        return redirect(url_for("informacion"))
    return render_template("datos.html",formulario=miformulario)


if __name__ == '__main__':
    app.run(debug=True,port=5000)
