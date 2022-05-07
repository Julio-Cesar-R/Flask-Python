#---------Librerias------------------
#Rutas
from flask import Flask
#Api
from flask_restful import Resource, Api
from requests import delete
#------------------------------------------
#Inicializar instancias a librerias
app=Flask(__name__)
api=Api(app)

personas=[]
class Persona(Resource):
    def get(self,valor):
        for persona in personas:
            if persona==valor:
                #Regresa un diccionario
                return {"Nombre": persona}
        return {"resultado":"Persona no encontrada"}

    def post(self,valor):
        persona=valor
        personas.append(valor)
        return {"resultado":"Persona añadida"}

    def delete(self,valor):
        for indice,persona in enumerate(personas):
            if persona==valor:
                personas.pop(indice)
        return {"resultado":"Persona eliminada de la lista"}

class Lista(Resource):
    def get(self):
        return {"resultado":personas}
api.add_resource(Persona,"/persona/<string:valor>")
api.add_resource(Lista,"/lista")


#Valida que la app se ejecute desde este fichero
if __name__=="__main__":
    app.run(debug=True)