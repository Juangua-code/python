# Solicitar el sueldo del trabajador
sueldo = float(input("Ingrese su salario actual: "))

if sueldo < 300000:
    aumento = sueldo * 0.15
    sueldo_final = sueldo + aumento
    print("El sueldo es inferior a $300,000, se le aplica un aumento del 15% y queda en un total de ",sueldo_final)
else:
    print("El sueldo es de $",sueldo, "y por ende no recibe aumento.")
