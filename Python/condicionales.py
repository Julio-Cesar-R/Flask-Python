#condicionales
condicion=True
if condicion:
    print("la condicion es verdadera")
else:
    print("la condicion es falsa")

if 5>55:
    print("Condicion verdadera")
else:
    print("condicion falsa")

numero1=int(input("Ingresa un numero :"))
numero2=int(input("ingresa otro numero :"))
if numero1==numero2:
    print("los numeros son iguales")
elif numero1>numero2:
    print(f"el numero {numero1} es mayor que el numero {numero2}")
else:
    print(f" el numero {numero1} es menor al numero {numero2}")    