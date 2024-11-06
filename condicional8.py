#revise cual es el numero del medio
a=int(input("digite el primer numero"))
b=int(input("Digite el segundo numero"))
c=int(input("digite el tercer numero"))

if(a>b and a<c) or (a<b and a>c):
        print("el numero del medio es",a)
elif (b>a and b<c)or (b< a and b>c):
        print("el numero del medio",b)
else:
        print("el numero del medio es",c)