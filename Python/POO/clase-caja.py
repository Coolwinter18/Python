class Caja:
    def __init__(self, ancho, alto, profundo):
        self.ancho = ancho
        self.alto = alto
        self.profundo = profundo

    def calcular_volumen(self):
        return self.ancho * self.alto * self.profundo

ancho = int(input("Proporciona el ancho: "))
alto = int(input("Proporciona el alto: "))
profundo = int(input("Proporciona lo profundo: "))

caja = Caja(ancho, alto, profundo)

print("resultado volumen caja:", caja.calcular_volumen())