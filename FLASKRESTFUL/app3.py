#---------Librerias------------------
#Rutas
from flask import Flask, jsonify
#Api
from flask_restful import Resource, Api
from numpy import append
from requests import delete
#------------------------------------------
#Inicializar instancias a librerias
app=Flask(__name__)
api=Api(app)

personas={"id":"1","nombre":"Kaiser"},{"id":"2","nombre":"Fox"}
class Persona(Resource):
    def get(self,**kargs):
        for persona in personas:
            if kargs["id"]== persona["id"]:
                return jsonify ({"resultado":persona})
        

    def delete(self,**kargs):
        for persona in personas:
            if kargs["id"]== persona["id"]:
                perdb=dict(persona)
                print(type(perdb))
                perdb.pop()
                return jsonify ({"resultado":perdb})
        

'''
     def post(self,**kargs):
        nuevo_dic={"id":kargs["id"],"nombre":kargs["nombre"]}
        print(nuevo_dic)
        personas= nuevo_dic
        return jsonify({"resultado":personas})'''

class Lista(Resource):
   def get(self):      
       return {"resultado":personas}
api.add_resource(Persona,"/persona/<id>,<nombre>")
api.add_resource(Lista,"/lista")


#Valida que la app se ejecute desde este fichero
if __name__=="__main__":
    app.run(debug=True)