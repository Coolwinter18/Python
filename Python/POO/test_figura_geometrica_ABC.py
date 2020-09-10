from herencia_multiple_ABC.cuadrado_ABC import Cuadrado
from herencia_multiple_ABC.figura_geometrica_ABC import FiguraGeometrica

#No se puede instanciar una clase abstracta
#figuraGeometrica = FiguraGeometrica(3,4)

cuadrado = Cuadrado(4, "rojo")
print(cuadrado.area())
print(cuadrado.color)

#Method Resolution Order
print(Cuadrado.mro())