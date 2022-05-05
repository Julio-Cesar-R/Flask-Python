#-----------------------LIBRERIAS---------------------------
#Ruta de la base
import os
#Formularios FlaskForm
from formulario import FormularioAlta, FormularioBaja
#Librerias de la api
from flask import Flask, render_template, redirect, url_for
# Conexion a base de datos
from flask_sqlalchemy import SQLAlchemy
#Libreria para hacer la migracion de datos
from flask_migrate import Migrate
#------------------------------------------------------------------
#-----------------------API Y CONFIGURACIONES-------------------------
#Ruta donde se creara la base
directorio = os.path.abspath(os.path.dirname(__file__))
# Definimos la app
app = Flask(__name__,template_folder="../template")
#Clave secreta
app.config['SECRET_KEY'] = 'clavesecreta'

#Configuraciones  de la app con SQLACHEMY
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(directorio,'gestion_mascotas.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Variable que hace referencia a la base
basededatos = SQLAlchemy(app)

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
#-------------------------------------------------------------------------
#-----------------------MODELO DE LA BASE---------------------------------
#Creacion de tablas
class Mascota(basededatos.Model):
    __tablename__ = 'Mascotas'
    id = basededatos.Column(basededatos.Integer, primary_key = True)
    nombre = basededatos.Column(basededatos.Text)
    #Constructor
    def __init__(self,nombre):
        self.nombre = nombre
    #Mensaje de la clase
    def __repr__(self):
        texto = " Mascota : nombre {}".format(self.nombre)
        return texto
#---------------------------------------------------------------------------------

#----------------------------RUTAS---------------------------------------------
# Vistas o rutas de la aplicacion
@app.route('/')
def principal():
    return render_template('vista_principal.html')

@app.route('/lista')
def lista():
    #Select a la base de datos
    mascotas = Mascota.query.all()
    return render_template('vista_lista.html',mascotas=mascotas)

@app.route('/alta',methods=['GET','POST'])
def alta():
    formulario = FormularioAlta()
    if formulario.validate_on_submit():
        nombre = formulario.nombre.data
        mascota = Mascota(nombre)
        #Insertar en la base
        basededatos.session.add(mascota)
        basededatos.session.commit()

        return redirect(url_for('lista'))

    return render_template('vista_alta.html',formulario=formulario)

@app.route('/borrar',methods=['GET','POST'])
def borrar():
    formulario = FormularioBaja()
    if formulario.validate_on_submit():
        id = formulario.id.data
        mascota_borrar = Mascota.query.get(id)
        basededatos.session.delete(mascota_borrar)
        basededatos.session.commit()

        return redirect(url_for('lista'))

    return render_template('vista_borrar.html',formulario=formulario)
#-----------------------------------------------------------------------------------
#Instruccion de la app para ejecutar el servicio
if __name__ == '__main__':
    app.run(debug=True)
