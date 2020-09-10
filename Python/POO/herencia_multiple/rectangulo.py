from figura_geometrica import FiguraGeometrica
from color import Color

class Rectangulo(FiguraGeometrica, Color):
    def __init__(self, alto,ancho, color):
        FiguraGeometrica.__init__(self, ancho, alto)
        #hace referencia a FiguraGeometrica por la prioridad
        #super().__init__(lado, lado) 
        Color.__init__(self, color)
    
    def area(self):
        return self.get_alto() * self.get_ancho()
    def __str__(self):
        return "Este Rectangulo tiene un ancho de "+str(self.get_ancho())+"y un alto de " +str(self.get_alto())+",y es de color"+str(self.get_color())