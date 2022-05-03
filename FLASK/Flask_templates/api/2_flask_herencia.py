#Estas apis mandan llamar urls las cuales dentro de la estructura mandar llamar de nuevo a las apis

from flask import Flask, render_template,request


app=Flask("__name__",template_folder="../template/tem_herencia",static_folder="../static")#lugar donde se almacenan los templates


@app.route("/pagina1")
def pagina1():
    return render_template("pagina1.html")

@app.route("/pagina2")
def pagina2():
     return render_template("pagina2.html")

@app.route("/formulario")
def formulario():
     return render_template("formulario.html")

@app.route("/gracias")
def gracias():
    #Recuperar informacion de un formulario
    valor1=request.args.get("nombre")
    valor2=request.args.get("apellidos")
    return render_template("gracias.html",name=valor1,lastname=valor2)#Enviamos las variables a gracias.html
#MANEJO DE ERRORES
@app.errorhandler(404)
def pagina_no_encontrada(e):
    return render_template("pagina404.html"),404



if __name__=="__main__":
    app.run(debug=True,port=5000)