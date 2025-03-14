from subclases.coche import Coche
from subclases.bicicleta import Bicicleta
from subsubclases.camioneta import Camioneta
from subsubclases.motocicleta import Motocicleta
from lanzador import  lanzador_main





def mostrar_menu():
	print("Seleccione el tipo de vehículo:")
	print("1. Coche")
	print("2. Bicicleta")
	print("3. Camioneta")
	print("4. El flipao de la moto del Valle del Kas")
	print("5. Salir")

def obtener_datos_vehiculo(tipo):
	if tipo == 1:
		# Obtener datos específicos para Coche
		marca = input("Ingrese la marca del coche: ")
		modelo = input("Ingrese el modelo del coche: ")
		return Coche(marca, modelo)
	elif tipo == 2:
		# Obtener datos específicos para Bicicleta
		marca = input("Ingrese la marca de la bicicleta: ")
		tipo_bici = input("Ingrese el tipo de bicicleta: ")
		return Bicicleta(marca, tipo_bici)
	elif tipo == 3:
		# Obtener datos específicos para Camioneta
		marca = input("Ingrese la marca de la camioneta: ")
		capacidad = input("Ingrese la capacidad de la camioneta: ")
		return Camioneta(marca, capacidad)
	elif tipo == 4:
		# Obtener datos específicos para Motocicleta
		marca = input("Ingrese la marca de la motocicleta: ")
		cilindrada = input("Ingrese la cilindrada de la motocicleta: ")
		return Motocicleta(marca, cilindrada)
	else:
		return None

if __name__ == "__main__":
	while True:
		mostrar_menu()
		opcion = int(input("Seleccione una opción: "))
		if opcion == 5:
			break
		vehiculo = obtener_datos_vehiculo(opcion)
		if vehiculo:
			print(f"Vehículo creado: {vehiculo}")
		else:
			print("Opción no válida, intente de nuevo.")
	lanzador_main()




