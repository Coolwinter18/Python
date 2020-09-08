#Imprimir solo la letra a 
for letra in "Holanda":
    if letra == "a":
        print(letra)
else:
    print("Fin ciclo for1")        

#Encontrar la primer letra a y terminar 
for letra in "Holanda":
    if letra == "a":
        print(letra)
        break
else:
    print("Fin ciclo for2")        

#Imprimir numeros solo numeros pares en un rango
for i in range(6):
    if i%2 == 0:
        print(i)    
        
#Usando continue 		
for i in range(6):
    if i%2 != 0:
        continue    
    print(i)