from subclases.coche import Coche
from subclases.bicicleta import Bicicleta
from subsubclases.camioneta import Camioneta
from subsubclases.motocicleta import Motocicleta
from superclases.vehiculo import Vehiculo

def lanzador_main():
    vehiculos = []

    vehiculos.append(Coche("rojo", 4, 150, 1200))
    vehiculos.append(Coche("azul", 4, 200, 2000))
    vehiculos.append(Bicicleta("verde", 2, "bh", "bmx", "urbana"))
    vehiculos.append(Bicicleta("blanca", 2, "orbea", "r2", "deportiva"))
    vehiculos.append(Camioneta("negro", 4, 100, 2200, "ford", "ranger", 1000))
    vehiculos.append(Moto)



    def catalogar(vehiculos, ruedas=None):
        if ruedas is not None:
            vehiculos_filtrados = [v for v in vehiculos if v.ruedas == ruedas]
            print(f"Se han encontrado {len(vehiculos_filtrados)} vehículos con {ruedas} ruedas:")
            for v in vehiculos_filtrados:
                print(f"{v.__class__.__name__}: {vars(v)}")
        else:
            for v in vehiculos:
                print(f"{v.__class__.__name__}: {vars(v)}")





