
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def division(a, b):
    if b == 0:
        input("ERROR, no es posible dividir por cero")
    return a / b

def multiplicacion(a, b):
    return a*b

def factorial(n):
    if n < 0:
        input("No es posible calcular el factorial de un número negativo")
    resultado = 1
    for i in range (1, n + 1):
        resultado *= i
    return resultado
