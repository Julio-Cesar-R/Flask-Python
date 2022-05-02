#funciones
import re


def funcion():
    print("Hola munndo")
funcion()

def sumar(num1,num2):
    """
    Esta funcion suma dos numeros enteros
    Ejemplo:
    sumar(23,45)
    """
    if type(num1)== type(num2)==type(10):
        res=0
        res=num1+num2
        return res
    else:
        return f"Uno de los valores que estas ingresando no es correcto\nnum1 {type(num1)} num2 {type(num2)}"


sum_res=sumar("hi",56)
print(f"El resultado de la suma es {sum_res}")