#Expresiones regulares
import re

texto="Este coche verde es muy rapido"
patron="verde"#expresion que se buscara en el texto
encontrado=re.search(patron,texto)
print(encontrado)
if encontrado:
    print(f"Patron '{patron}' encontrado en el texto")
    print(f"El patron comienza en la posicion: {encontrado.start ()}")
    print(f"El patron termina en la pisicion: {encontrado.end()}")
else:
    print(f"Patron {patron} no encontrado")


#Encontrar todas las coincidencias
texto2=" me gusta el color verde y por eso he comprado pintura verde"
patron2="verde"
encontrado2=re.findall(patron2,texto2)
print(encontrado2)
repeticiones=len(encontrado2)
print(f"Numero de coincidencias: {repeticiones}")


texto3="me gusta el color verde y por eso he comprado pintura verde"
patrones=["gusta","color","verde"]
for n in patrones:
    encontrado3=re.findall(n,texto3)
    print(f"Patron '{n}' encontrado  Repeticiones: {len(encontrado3)}")

