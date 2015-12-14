#By Svaazz

import os
import bone
sitio = ""

def main(direccion):
	global archivo
	os.system("clear")
	print("""\
		################ Escaner Web ###############
		URL actual: """, direccion, """
		############################################
		0. Salir.")
		1. Buscar cadena de caracteres.
		2. Guardar contenido en el disco.
		3. Cambiar url.
		4. Escanear puertos abiertos. (Necesaria IP)
	   	############################################
	    """)
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
