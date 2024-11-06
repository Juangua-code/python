n1=float(input("Su primera nota fue de: "))
n2=float(input("Su segunda nota fue de: "))
n3=float(input("Su tercera nota fue de: "))
    
nota_total = (n1 + n2 + n3) / 3
    
if nota_total >= 3.0:
        resultado = "Aprobado"
else:
        resultado = "Reprobado"
    
print("La nota de su materia es de: ",nota_total,"por ende su materia esta ",resultado)