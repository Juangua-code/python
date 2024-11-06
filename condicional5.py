#revisar entre 3 numeros cual es mayor,meno e iguales
Num1= int(input("digite un numero"))
Num2= int(input("Digite un segundo numero"))
Num3=int(input("Digite un tercer numero"))

mayor= max(Num1,Num2,Num3)
menor= min (Num1,Num2,Num3)

if Num1==Num2==Num3:
    print("los tres numeros son iguales")
elif Num1!=Num2 !=Num3 and Num1!=Num3:
    print("los tres numeros son diferentes")
    if Num1 == Num2:
        print("Los números ",Num1 and Num2, "son iguales.")
    elif Num1 == Num3:
        print("Los números ",Num1 and Num3, "son iguales.")
    elif Num2 == Num3:
        print("Los números",Num2 and Num3, "son iguales.")

print("El número mayor es: ",mayor)
print("El número menor es: ",menor)