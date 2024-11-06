import math

a=float(input("digite el primer numero: "))
b=float(input("digite el segundo numero: "))
c=float(input("digite el tercer numero"))
    # Verificar que a no sea cero para que sea una ecuación cuadrática válida
if a == 0:
    print ("Error: a no puede ser cero en una ecuación cuadrática")
    
    discriminante = b**2 - 4 * a * c
    
   
    if discriminante < 0:
     print("No hay soluciones reales")
    elif discriminante == 0:
        # Una sola solución real (raíces iguales)
        x = -b / (2 * a)
        print(f"Solución única: x = {x}")
    else:
        # Dos soluciones reales
        x1 = (-b + math.sqrt(discriminante)) / (2 * a)
        x2 = (-b - math.sqrt(discriminante)) / (2 * a)
        print (f"Soluciones: x1 = {x1}, x2 = {x2}")