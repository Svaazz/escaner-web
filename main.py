#By Svaazz

import os
import bone
import lang
sitio = ""

def main(direccion):
	global archivo
	bone.limpiar()
	print(lang.main('cabecera1'), direccion, lang.main('cabecera2'))
		
	print(lang.main('menu1'))
	eleccion = input(">> ")
	if eleccion == "1":
		bone.buscar(direccion)
		main(direccion)
	elif eleccion == "2":
		print(lang.main('nArch'))
		archivo = input(str(">> "))
		if archivo == "":
			archivo = "SinNombre.html"
		print(lang.main('elArch'), archivo, lang.main('sCreado'))
		bone.conectar(direccion, archivo)
		main(direccion)
	elif eleccion == "3":
		url(lang.main('cambUrl'))
	elif eleccion == "0":
		bone.limpiar()
		print(lang.main('saliendo'))
		exit()
	elif eleccion == "4":
		bone.puertos(direccion)
		main(direccion)
	elif eleccion == "5":
		bone.navegador(direccion)
		main(direccion)
	else:
		main(direccion)

def url(error = ""):
	bone.limpiar()
	print(error)
	print("")
	print(lang.main('intUrl'))
	sitio = input(str(">> "))
	if sitio.startswith("http://") or sitio.startswith("https://") and sitio.find('.') != -1:
		main(sitio)
	elif sitio.find('.') == -1:
		url(lang.main('errUrl'))
	else:
		sitio = "http://" + sitio
		main(sitio)
url()
