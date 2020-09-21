from orden import Orden
from computadora import Computadora
from monitor import Monitor
from raton import Raton
from teclado import Teclado

tecladoHp = Teclado("Hp", "usb")
ratonHp = Raton("Hp", "usb")
monitorHp = Monitor("Hp", "15 pulgadas")
computadoraHp = Computadora("Hp", monitorHp, tecladoHp, ratonHp)

tecladoAcer = Teclado("Acer", "bluetooth")
ratonAcer = Raton("Acer", "bluetooth")
monitorAcer = Monitor("Acer", "27 pulgadas")
computadoraAcer = Computadora("Acer", monitorAcer, tecladoAcer, ratonAcer)

tecladoGamer = Teclado("Gamer", "bluetooth")
ratonGamer = Raton("Gamer", "bluetooth")
monitorGamer = Monitor("Gamer", "45 pulgadas")
computadoraGamer = Computadora("Gamer", monitorGamer, tecladoGamer, ratonGamer)

computadoras_orden1 = [computadoraHp, computadoraAcer]
orden1=Orden(computadoras_orden1)
print(orden1)

computadoras_orden2 = [computadoraGamer]
orden2 = Orden(computadoras_orden2)
orden2.agregar_computadora(computadoraHp)
print(orden2)