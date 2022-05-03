#Esta api muestra dos valores de variables almacenados en un servicio web

from flask import Flask
app=Flask("__name__")

@app.route("/datos/<nombre>/<edad>")
def datos(nombre, edad):
    return f"<h2>Tu nombre es {nombre} y tu edad es {edad} </h2>"

if __name__==("__main__"):
    app.run(debug=True,port=5000)