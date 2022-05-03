# una api que calcule la longuitud de una palabra dada
from flask import flash
from flask import Flask
app=Flask("__name__")

@app.route("/longitud/<palabra>")
def longuitud(palabra):
    return f"<h2>La palabra {palabra} tiene una longuitud de {len(palabra)} caracteres</h2>"

if __name__=="__main__":
    app.run(debug=True,port=5000)