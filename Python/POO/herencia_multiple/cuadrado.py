from figura_geometrica import FiguraGeometrica
from color import Color

class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        FiguraGeometrica.__init__(self, lado, lado)
        #hace referencia a FiguraGeometrica por la prioridad
        #super().__init__(lado, lado) 
        Color.__init__(self, color)
    
    def area(self):
        return self.get_alto() * self.get_ancho()
    def __str__(self):
        return "Este cuadrado tiene un lado de "+str(self.get_ancho()) +",y es de color"+str(self.get_color())