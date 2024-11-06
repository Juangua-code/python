# Capturar los datos de la persona
nombre = input("Ingrese el nombre: ")
edad = int(input("Ingrese la edad: "))
sexo = input("Ingrese el sexo (M para masculino, F para femenino): ").upper()
estado_civil = input("Ingrese el estado civil (soltero/a o casado/a): ").lower()

# Verificar las condiciones para imprimir el nombre según el criterio dado
if (sexo == 'M' and estado_civil == "casado" and edad > 40):
    print("{nombre} es un hombre casado mayor de 40 años.")
elif (sexo == 'F' and estado_civil == "soltera" and edad < 50):
    print("{nombre} es una mujer soltera menor de 50 años.")
else:
    print("La persona no cumple con los criterios especificados.")