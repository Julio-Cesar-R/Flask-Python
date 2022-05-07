#---------Librerias------------------
#Rutas
from flask import Flask
#Api
from flask_restful import Resource, Api
#------------------------------------------
#Inicializar instancias a librerias
app=Flask(__name__)
api=Api(app)
#Clase
class Saludar(Resource):
    #Metodo de la clase y tipo de peticion
    def get(self):
        return {"saludo":"Buenos dias"}
#Api ruta
# vincula la clase con la ruta
api.add_resource(Saludar,"/")

#Valida que la app se ejecute desde este fichero
if __name__=="__main__":
    app.run(debug=True)