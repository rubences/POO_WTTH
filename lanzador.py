from subclases.coche import Coche
from subclases.bicicleta import Bicicleta
from subsubclases.camioneta import Camioneta
from subsubclases.motocicleta import Motocicleta


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

def catalogar(vehiculos, ruedas=None):
    if ruedas is not None:
        vehiculos_filtrados = [v for v in vehiculos if v.ruedas == ruedas]
        print(f"Se han encontrado {len(vehiculos_filtrados)} vehículos con {ruedas} ruedas:")
        for vehiculo in vehiculos_filtrados:
            print(f"Clase: {vehiculo.__class__.__name__}")
            for atributo, valor in vehiculo.__dict__.items():
                print(f"{atributo}: {valor}")
            print()
    else:
        for vehiculo in vehiculos:
            print(f"Clase: {vehiculo.__class__.__name__}")
            for atributo, valor in vehiculo.__dict__.items():
                print(f"{atributo}: {valor}")
            print()


def mostrar_menu():
	print("Seleccione el tipo de vehículo:")
	print("1. Coche ")
	print("2. Bicicleta")
	print("3. Camioneta")
	print("4. Motocicleta")
	print("5. Ordenar por tipo de ruedas")
	print("6. Salir")

def obtener_datos_vehiculo(tipo):
	if tipo == 1:
		# Obtener datos específicos para Coche
		color = input("Ingrese el color del coche: ")
		ruedas = input("Ingrese el numero de ruedas del coche: ")
		velocidad = input("Ingrese la velocidad del coche: ")
		cilindrada = input("Ingrese la cilindrada del coche: ")
		vehiculo.append(Coche(color, ruedas, velocidad, cilindrada))
		return Coche(color, ruedas, velocidad, cilindrada)
	elif tipo == 2:
		# Obtener datos específicos para Bicicleta
		color = input("Ingrese el color de la bicicleta: ")
		ruedas = input("Ingrese el numero de ruedas de la bicicleta: ")
		marca = input("Ingrese la marca de la bicicleta: ")
		modelo = input("Ingrese el modelo de la bicicleta: ")
		tipo = input("Ingrese el tipo de la bicicleta: ")
		
		return Bicicleta(color, ruedas, marca, modelo, tipo)
	elif tipo == 3:
		# Obtener datos específicos para Camioneta
		color = input("Ingrese el color de la camioneta: ")
		ruedas = input("Ingrese el numero de ruedas de la camioneta: ")
		velocidad = input("Ingrese la velocidad de la camioneta: ")
		cilindrada = input("Ingrese la cilindrada de la camioneta: ")
		marca = input("Ingrese la marca de la camioneta: ")
		modelo = input("Ingrese el modelo de la camioneta: ")
		carga = input("Ingrese la carga de la camioneta: ")
		
		return Camioneta(color, ruedas, velocidad, cilindrada, marca, modelo, carga)
	elif tipo == 4:
		# Obtener datos específicos para Motocicleta
		color = input("Ingrese el color de la motocicleta: ")
		ruedas = input("Ingrese el numero de ruedas de la motocicleta: ")
		marca = input("Ingrese la marca de la motocicleta: ")
		modelo = input("Ingrese el modelo de la motocicleta: ")
		tipo = input("Ingrese el tipo de la motocicleta: ")
		velocidad = input("Ingrese la velocidad de la motocicleta: ")
		cilindrada = input("Ingrese la cilindrada de la motocicleta: ")
		
		return Motocicleta(color, ruedas, marca, modelo, tipo, velocidad, cilindrada)
	
	elif tipo == 5:
		# Ordenar por tipo de ruedas
		ruedas = int(input("Ingrese el número de ruedas para filtrar: "))
		catalogar(vehiculos=[], ruedas=ruedas)
		return None

	else:
		return None






