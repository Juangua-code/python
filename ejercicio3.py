#calcular puntaje de un equipo de futbol en un torneo
PG = int(input("Cantidad de partidos ganados"))
PP = int(input("Cantidad de partidos perdidos"))
PE = int(input("cnatidad de partidos empatados"))

TPG= PG*3
TPP= PP*0
TPE= PE*1

PuntosTotales = TPG+TPP+TPE
print ("Puntaje total del equipo es de",PuntosTotales,)