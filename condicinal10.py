#calcular la calificacion final de un estudiantes
n1=float(input("Escriba su primera nota"))
n2=float(input("Escriba su segunda nota"))
n3=float(input("Escriba su tercera nota"))

if n1 <= n2 and n1 <=n3:
    promedio= (n2+n3)/2
    print("su nota es de: ",promedio)
elif n2 <=n1 and n2 <=n3:
    promedio=(n1+n3)/2
    print("su nota final es de: ",promedio)
else:
    promedio=(n1+n2)/2
    print("su nota final es de: ",promedio)