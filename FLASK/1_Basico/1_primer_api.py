#API

from flask import Flask

app=Flask(__name__)
#Crear rutas
@app.route("/")
def principal():
    return "<h1> Bienvenido Kaiser esta es tu primer api</h1>"

@app.route("/adios")
def adios():
    return "<h2> Adios amigo </h2>"

#Rutas dinamicas, rutas con variables
@app.route("/saludar/<nombre>")#Nombre es una variable
def saludo(nombre):
    return f"<h2> Hola {nombre} buenos dias </h2>"

#ERRORES " app.run(debug=True,port=5000)"
#Posicion de una palabra
@app.route("/posicion/<nombre>")#Nombre es una variable
def posicion(nombre):
    return f"<h2> La posicion 2 de la palabra {nombre}  es: {nombre[7]} </h2>"




#Correr el programa  
if __name__=="__main__":
    app.run(debug=True,port=5000)#Debuj true es solo para la aplicacion local en web no