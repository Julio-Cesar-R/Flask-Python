#VALIDACION DE MAYUSCULAS MINUSCULAS Y NUMEROS
from flask import Flask, render_template,request
import re
app=Flask("__name__",template_folder="../template/")#lugar donde se almacenan los templates



@app.route("/formulario")
def formulario():
     return render_template("formulario.html")

@app.route("/respuesta")
def respuesta():
    #Recuperar informacion de un formulario
    nombre=request.args.get("nombre")
    #Validacion
    minuscula=any(letra.islower() for letra in nombre)
    numero= any(numero.isdigit()for numero in nombre)
    mayuscula=nombre[0].isupper()
    longuitud=len(nombre)>6
    todo= minuscula and numero and mayuscula and longuitud
    
    return render_template("respuesta.html",coincidencia=todo,minuscula=minuscula,
    numero=numero,longuitud=longuitud,mayuscula=mayuscula)#Enviamos las variables a gracias.html



if __name__=="__main__":
    app.run(debug=True,port=5000)