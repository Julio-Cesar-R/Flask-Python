#FLASK FORM pip install Flask_WTF

#Flask y render template
from flask import Flask, render_template
#Clase de tipo flask form
from flask_wtf import FlaskForm
#Campos de formulario
from wtforms import StringField, SubmitField 

#Iniciamos nuestra aplicacion
app = Flask("__name__",template_folder="../template/")
#clave secreta de app
app.config['SECRET_KEY'] = 'clavesecreta'

#Formulario
class Formulario(FlaskForm):
    nombre = StringField("Nombre") 
                                
    enviar = SubmitField("Enviar")

#Aplicacion Flask
@app.route('/',methods=['GET','POST'])#Se puede accesar a esta ruta por estos dos metodos
def principal():
    nombre = ''
    
    enviado = False
    formulario = Formulario()

    #Validar si el formulario ha sido enviado
    if formulario.validate_on_submit():
        enviado = True
        nombre = formulario.nombre.data
        
        formulario.nombre.data = ''
    #Envia el formulario , nombre y apellido y enviado a index.html
    return render_template('index.html',formulario=formulario, nombre=nombre,enviado=enviado)

if __name__ == '__main__':
    app.run(debug=True)
