#FLASK CON BOOTSTRAP

from flask import Flask, render_template, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask("__name__",template_folder="../template")

app.config['SECRET_KEY'] = 'miclave'

class Formulario(FlaskForm):
    nombre=StringField("Nombre")
    boton=SubmitField("Enviar mensaje")


@app.route('/mensaje',methods=['GET','POST'])
def mensaje():
	formulario = Formulario()
	if formulario.validate_on_submit():
		nombre=formulario.nombre.data
		flash(f"Gracias {nombre}, por pulsar el boton ")
		return redirect(url_for("mensaje"))       

	return render_template('mensaje.html',formulario=formulario)

if __name__ == '__main__':
	app.run(debug=True)
