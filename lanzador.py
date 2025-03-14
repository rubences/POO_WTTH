from subclases.coche import Coche
from subclases.bicicleta import Bicicleta
from subsubclases.camioneta import Camioneta
from subsubclases.motocicleta import Motocicleta

def lanzador_main():
    vehiculos = []

    mi_vehiculo = Coche("Rojo", 4, 180, 2000)
    vehiculos.append(mi_vehiculo)
    print(mi_vehiculo)

    mi_vehiculo2 = Bicicleta("Azul", "Montaña", "Azul", "Deportiva",2)
    vehiculos.append(mi_vehiculo2)
    print(mi_vehiculo2)

    mi_vehiculo3 = Camioneta("Ford", "Fiesta", "Blanco", 4, 1000, 160, 2500)
    vehiculos.append(mi_vehiculo3)
    print(mi_vehiculo3)

    mi_vehiculo6 = Bicicleta("Rojo", "Carretera", "Rojo", "Competición",2)
    
    vehiculos.append(mi_vehiculo6)
    print(mi_vehiculo6)

    mi_vehiculo7 = Camioneta("Chevrolet", "Silverado", "Negro", 4, 1500, 140, 3000)
    vehiculos.append(mi_vehiculo7)
    print(mi_vehiculo7)

    mi_vehiculo8 = Motocicleta("Honda", "Blanca", "Touring", 2, 1200, "Touring")

    vehiculos.append(mi_vehiculo8)
    print(mi_vehiculo8)

    mi_vehiculo4 = Motocicleta("Yamaha", "Negra", "Deportiva", 2, 1000, "Deportiva")
    vehiculos.append(mi_vehiculo4)
    print(mi_vehiculo4)

    def catalogar(vehiculos, ruedas=None):
        if ruedas is not None:
            vehiculos_filtrados = [v for v in vehiculos if v.ruedas == ruedas]
            print(f"Se han encontrado {len(vehiculos_filtrados)} vehículos con {ruedas} ruedas:")
            for v in vehiculos_filtrados:
                print(v)
        else:
            for v in vehiculos:
                print(v)

    catalogar(vehiculos)
    catalogar(vehiculos, 0)
    catalogar(vehiculos, 2)
    catalogar(vehiculos, 4)




