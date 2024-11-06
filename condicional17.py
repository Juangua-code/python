n1=int(input("Digite el primer numero"))
n2=int(input("Digite el segundo numero"))
n3=int(input("Digite el tercer numero"))

if n1 % n2 == 0:
        print(n1," es divisible por ",n2)
elif n1 % n3 == 0:
        print(n1," es divisible por ",n3)
elif n2 % n1 == 0:
        print(n2," es divisible por ",n1)
elif n2 % n3 == 0:
        print(n2," es divisible por " ,n3)
elif n3 % n1 == 0:
        print(n3," es divisible por " ,n1)
elif n3 % n2 == 0:
       print(n3, "es divisible por ",n2)
else:
        print("Ningún número es divisible por otro")