#ordenar de mayor a menos los numeros
a= float(input("digite el primer numero"))
b=float(input("digite el segundo numero"))
c=float(input("digite el tercer numero"))
if a<b and a<c:
    if b<c:
        print(a,b,c)
    else:
        print(a,c,b)
elif b<a and b<c:
    if a<c:
        print(b,a,c) 
    else:
        print(b,c,a)
else:
    if a<b:
        print(c,a,b)
    else:
        print(c,b,a)    