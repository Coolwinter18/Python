condicion = False

#Operacion ternaria // simplificada de if

print("Operacion Verdadera") if condicion else print("Condicion Falsa")
if condicion == True:
    print("La condicion es verdadera")
elif(condicion == False):
    print("la condicion es falsa")
else:
    print("Condicion no reconocida")

numero = int(input("Proporciona un numero  entre 1 y 3: "))

if numero == 1:
    numeroTexto = "numero uno"
elif numero == 2:
    numeroTexto = "numero dos"
elif numero == 3:
    numeroTexto = "Valor fuera de rango"
    
print("numero proporcionado: ",numeroTexto)



