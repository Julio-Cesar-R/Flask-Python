
from flask import Flask,render_template
#Se agregan las rutas de los templates y de las imagenes (template_folder="../template",static_folder="../static")
app=Flask("__name__",template_folder="../template",static_folder="../static")

@app.route("/")
def portada():
    nombre="Kaiser Fox"#Variable que se incluira en la pagina
    edad=34
    ocupacion="Desarrollador web"
    #Creacion del diccionario
    diccionario={"name":nombre,"edge":edad,"job":ocupacion}
    #Carga la ruta de la pagina html
    return render_template("portada.html",datos=diccionario)#pasa el diccionario
  
@app.route("/hola")
def hola():
    valor="Kaiser Fox"#Variable que se incluira en la pagina
    edad=34
    return render_template("hola.html",name=valor.upper(),edad=edad)#name es la variable que enviaremos al template

@app.route("/colores")
def colores():
    #Uso de listas
    list_colores=["Rojo","Verde","Azul","Naranja"]
    return render_template("colores.html",colores=list_colores)

@app.route("/frases/<texto>")#Ruta y valor
def frases(texto):
    #uso de condicionales

    return render_template("frases.html",tipo=texto)



if __name__=="__main__":
    app.run(debug=True,port=5000)