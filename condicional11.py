diametro=float(input("Digite el diametro"))
longitud=float(input("digite la longitud"))

densidad = 3.5   
    
masa = (diametro * longitud) / densidad
    
if 7.5 < longitud <= 9.0 and 0.5 <= diametro <= 1.3 and masa <= 5.8:
        print ("Pieza aceptada")
else:
        print( "Pieza rechazada")