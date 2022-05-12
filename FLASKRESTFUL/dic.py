from turtle import update


dic={"id":1,"nombre":"juan"}
dic2={"id":2,"nombre":"j"}
d3={**dic,**dic2}
print(d3)


'''

personas={"id":"1","nombre":"Kaiser","edad":25},{"id":"2","nombre":"Fox","edad":30}

def agregar(valor):
    for indice,persona in enumerate(personas):
        if persona["id"]==valor["id"]:
            personas.popitem(indice)
            print(personas)


def per(**args):
    print(args)
    for persona in personas:
        if args["id"]==persona["id"]:
            print(persona["nombre"],persona["edad"])
        
        
dic={"'id':'3','nombre':'Lala','edad':12"}
agregar(dic)
        
#per(id="2")'''