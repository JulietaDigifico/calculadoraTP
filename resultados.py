from calculadora import suma, resta, division, multiplicacion, factorial

def ingresar_numero(mensaje):
    while True:
        entrada = input(mensaje) 
        if entrada.isdigit():
            return int(entrada)
        print("Entrada invalida, debe ingresar un numero entero")

def main():
    a = None
    b = None
    resultado_suma = None
    resultado_resta = None
    resultado_division = None
    resultado_multiplicacion = None
    resultado_factorial_a = None
    resultado_factorial_b = None
    calculo = None

    while True:
        print("\nCalculadora")
        print(f"1. Ingresar primer operando (A={a})")
        print(f"2. Ingresar segundo operando (B={b})")
        print("3. Calcular todas las operaciones")
        print("4. Informar resultados")
        print("5. Salir")

        opcion = input("Seleccione una opción: ").upper()

        if opcion == "1":
            a = ingresar_numero("Ingrese un número: ")
            calculo = False
        elif opcion == "2":
            b = ingresar_numero("Ingrese otro número: ")
            calculo = False
        elif opcion == "3":
            if a == None or b == None:
                print("Debe ingresar ambos números enteros")
            else:
                resultado_suma = suma(a, b)
                resultado_resta = resta(a, b)
                resultado_division = division(a, b)
                resultado_multiplicacion = multiplicacion(a, b)
                resultado_factorial_a = factorial(a) if a >= 0 else "No es posible calcular el factorial"
                resultado_factorial_b = factorial(b) if b >= 0 else "No es posible calcular el factorial"
                calculo = True
        elif opcion == "4":
            if not calculo:
                print("Debe calcular las operaciones primero")
            else:
                print(f"El resultado de la suma es: {resultado_suma}")
                print(f"El resultado de la resta es: {resultado_resta}")
                print(f"El resultado de la división es: {resultado_division}")
                print(f"El resultado de la multiplicación es: {resultado_multiplicacion}")
                print(f"El factorial de A es: {resultado_factorial_a}")
                print(f"El factorial de B es: {resultado_factorial_b}")
        elif opcion == "5":
            break
        else: 
            print("Opcion invalida, intente nuevamente")

if __name__ == "__main__":
    main()