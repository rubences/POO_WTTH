from subclases.coche import Coche
from subclases.bicicleta import Bicicleta
from subsubclases.camioneta import Camioneta
from subsubclases.motocicleta import Motocicleta
from superclases.vehiculo import Vehiculo

def lanzador_main():
    vehiculos = []

    vehiculos.append(Coche("Rojo", 4, 180, 2000))
    vehiculos.append(Bicicleta("Azul", 2, "Montaña", "Deportiva", "Azul"))
    vehiculos.append(Camioneta("Blanco", 4, 160, 2500, "Ford", "Fiesta", 1000))
    vehiculos.append(Bicicleta("Rojo",2, "Carretera", "Rojo", "Competición"))
    vehiculos.append(Camioneta("Chevrolet", 4, 1500, 140, "Silverado", "Negro", 3000))
    vehiculos.append(Motocicleta("Blanca", 2, "Honda", "Touring", "Touring", 180, 1200))
    vehiculos.append(Motocicleta("Roja", 2, "Yamaha", "Urbana", "Touring", 180, 1200))
    vehiculos.append(Camioneta("Toyota",  4, 2000, 150, "Hilux", "Gris", 2800))
    vehiculos.append(Bicicleta("Verde", 2, "Urbana", "Verde", "Paseo"))
    vehiculos.append(Motocicleta("Suzuki", "Azul", "Naked", 2, 750, "Naked"))
    vehiculos.append(Camioneta("Nissan", 4, 1800, 140, "Frontier", "Rojo", 2700))
    vehiculos.append(Bicicleta("Amarillo", 2,  "BMX", "Amarillo", "Freestyle"))
    vehiculos.append(Motocicleta("Kawasaki", "Verde", "Cruiser", 2, 900, "Cruiser"))
    vehiculos.append(Camioneta("Mitsubishi",  4, 1700, 130, "L200", "Azul", 2600))
    vehiculos.append(Bicicleta("Negro", 2, "Plegable", "Negro", "Urbana"))
    vehiculos.append(Motocicleta("Ducati", "Rojo", "Sport", 2, 1100, "Sport"))
    vehiculos.append(Camioneta("Isuzu", 4, 1900, 160, "D-Max", "Blanco", 2900))
    vehiculos.append(Bicicleta("Blanco", 2, "Eléctrica", "Blanco", "Urbana"))
    vehiculos.append(Motocicleta("BMW", "Gris", "Adventure", 2, 1200, "Adventure"))
    vehiculos.append(Camioneta("Volkswagen", 4, 2100, 170, "Amarok", "Negro", 3000))

    def catalogar(vehiculos, ruedas=None):
        if ruedas is not None:
            vehiculos_filtrados = [v for v in vehiculos if v.ruedas == ruedas]
            print(f"Se han encontrado {len(vehiculos_filtrados)} vehículos con {ruedas} ruedas:")
            for v in vehiculos_filtrados:
                print(f"{v.__class__.__name__}: {vars(v)}")
        else:
            for v in vehiculos:
                print(f"{v.__class__.__name__}: {vars(v)}")





