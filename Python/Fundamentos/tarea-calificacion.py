"""Si está entre 9 y 10: imprimir una A

Si está entre 8 y menor a 9: imprimir una B

Si está entre 7 y menor a 8: imprimir una C

Si está entre 6 y menor a 7: imprimir una D

Si está entre 0 y menor a 6: imprimir una F

cualquier otro valor debe imprimir: Valor desconocido
"""
calificacion = int(input("Proporcione una calificacion"))

if(calificacion >= 9 or calificacion <= 10):
    calificacion = "A"
elif(calificacion >= 8 or calificacion < 9):
    calificacion = "B"
elif(calificacion >= 7 or calificacion < 8):
    calificacion = "C"
elif(calificacion >= 6 or calificacion < 7):
    calificacion = "D"
elif(calificacion >= 0 or calificacion < 6):
    calificacion = "F"
else:
    calificacion = "valor desconocido"

print("Su nota es: ",calificacion)