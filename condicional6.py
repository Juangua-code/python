# Capturar el valor del usuario
ingreso= (input("digite los grados centigrados: "))
kelvin=float

if ingreso.isdigit() or (ingreso[0]== "-" and ingreso[1:].isdigit()):
    celsius=float(ingreso)
    Kelvin= celsius + 273.15
    print ("Los grados en Kelvin son: ",Kelvin)
    exit()

if ingreso.replace('.', '', 1).replace('-', '', 1).isdigit():
    celsius=float(ingreso)
    if celsius > 10.5 :
        print("El numero es mayor a 10.5")
    else:
        print("no es mayor a 10.5")
        exit()

if ingreso.isalpha():
    Nombre= input("Escriba su nombre: ")
    print(Nombre)

