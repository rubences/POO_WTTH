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
    vehiculos.append(Motocicleta("blanca",2,"Suzuki","GSXR", "Deportiva", 300, 999))
    
    catalogar(vehiculos)
    
def catalogar(vehiculos):
    for vehiculo in vehiculos:
        print(f"Clase: {vehiculo.__class__.__name__}")
        for atributo, valor in vehiculo.__dict__.items():
            print(f"{atributo}: {valor}")
        print()







