# Solicitar al usuario que ingrese un número
num1 = float(input("Ingrese un número: "))

if num1 < 0:
    print(f"Número negativo: {num1}")
    print(f"Número positivo: {-num1}")
else:
    print("El número ingresado no es negativo.")