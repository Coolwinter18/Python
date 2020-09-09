class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        
    def calcular_area(self): 
        return self.base * self.altura   
    
#base = int(input("Proporciona la base:"))
#altura = int(input("Proporciona la altura:"))

#rectangulo = Rectangulo(base, altura)  
rectangulo = Rectangulo(2, 3)  
print(rectangulo.calcular_area())  
print(id(rectangulo))

rectangulo1 = Rectangulo(4,2)
print(rectangulo1.calcular_area())
print(id(rectangulo1))