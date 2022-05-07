#----------------RUTAS DE LA APLICACION----------------------------
#----------------LIBRERIAS-----------------------------
#Base de datos y app
from conexion import app,basededatos
# Flask redirecciones
from flask import render_template, redirect, request, url_for, flash
#Rutas con login
from flask_login import login_user, login_required, logout_user
#Modelo  usario (base)
from modelos import Usuario
#Formularios
from formulario import Formulario_Registro,Formulario_Login
#Encriptacion
from werkzeug.security import generate_password_hash, check_password_hash

#------------------------------------------------------------------------
#----------------------------RUTAS----------------------------------
#Ruta principal
@app.route('/')
def principal():
    return render_template('principal.html')

#Bienvenido( hay que estar logeado)
@app.route('/bienvenido')
@login_required
def bienvenido():
    return render_template('bienvenido.html')

#Cerrar session
@app.route('/salir')
@login_required
def salir():
    logout_user()
    flash('Sessión de usuario cerrada')
    return redirect(url_for('principal'))

#Loguearse
@app.route('/entrar',methods=['GET','POST'])
def entrar():
    #Formulario
    formulario = Formulario_Login()
    if formulario.validate_on_submit():
        usuario = Usuario.query.filter_by(email=formulario.email.data).first()
        if usuario is not None:
            #Valida la contraseña encriptada
            if check_password_hash(usuario.password_encriptada, formulario.password.data):
                #Flask login , activa el usuario
                login_user(usuario)
                flash("Usuario ha entrado correctamente")
                #redirecciona a la pagina que eligio acceder y necesitaba estar logeado
                proxima = request.args.get('next')
                if proxima == None or not next[0] == '/':
                    proxima = url_for('bienvenido')
                return redirect(proxima)
    return render_template('entrar.html',formulario=formulario)

#Registrarse
@app.route('/registrar',methods=['GET','POST'])
def registrar():
    #Invocamos al formulario
    formulario = Formulario_Registro()
    if formulario.validate_on_submit():
        #Recupera la infoormacion del formulario
        usuario = Usuario(email=formulario.email.data, nombre=formulario.nombre.data,
                            password = formulario.password.data)
        #Registro a la base
        basededatos.session.add(usuario)
        basededatos.session.commit()
        flash("Usuario registrado correctamente")
        return redirect(url_for('entrar'))
    return render_template('registrar.html',formulario=formulario)


if __name__ == '__main__':
    app.run(debug=True)
