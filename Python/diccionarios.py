
#Diccionarios
dic={"clave1":4,"clave2":6,"clave3":5}
print(dic)
print(dic.keys())
print (dic.values())
print(dic["clave1"])

diccionario={"verde":"green","rojo":"red","Amarillo":"Yellow"}
print(diccionario["verde"])

for n in diccionario.keys():
    if n=="verde":
        print(diccionario[n])
    else:
        print("no hay coincidencia")
#reasignar un valor
diccionario["Amarillo"]="YELLOW"
print(diccionario)
#agregar un nuevo valor
diccionario["Negro"]="Black"
print(diccionario)