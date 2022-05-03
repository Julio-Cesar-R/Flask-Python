#Crea una funcion que convierta strings a int para sumarlos y mostrarlos
from turtle import st
from flask import Flask

app=Flask("__name__")

@app.route("/suma/<num1>/<num2>")
def suma(num1,num2):
    suma=int(num1)+int(num2)
    resultado=str(suma)
    return f"<h3>La suma de {num1} y {num2}  es: {resultado}</h3>"

if __name__=="__main__":
    app.run(debug=True,port=5000)