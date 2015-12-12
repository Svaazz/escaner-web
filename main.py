#By Svaazz

import os
import bone
sitio = ""

def main(direccion):
	global archivo
	os.system("clear")
	print("############By Svaazz#############")
	print("##################################")
	print("0. Salir.")
	print("1. Buscar cadena de caracteres.")
	print("2. Guardar contenido en el disco.")
	print("3. Cambiar url.")
	print("4. Escanear puertos abiertos. (Necesaria IP)")
	print("##################################")
	eleccion = input(">> ")
	if eleccion == "1":
		bone.buscar(direccion)
		main(direccion)
	elif eleccion == "2":
		print("Introduce un nombre para el archivo:")
		archivo = input(str(">> "))
		if archivo == "":
			archivo = "Contenido.txt"
		print("El archivo ", archivo, " esta siendo creado")
		bone.conectar(direccion, archivo)
		main(direccion)
	elif eleccion == "3":
		url()
	elif eleccion == "0":
		os.system("clear")
		print("Saliendo...")
		exit()
	elif eleccion == "4":
		bone.puertos(direccion)
		main(direccion)
	else:
		main(direccion)

def url():
	os.system("clear")

	print("Por favor introduce una URL: (http://ejemplo.com)")
	sitio = input(str(">> "))
	if sitio.startswith("http"):
		main(sitio)
	else:
		url()
url()
