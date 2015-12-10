#By Svaazz

import requests
import os
cntnd = ""
def conectar(sitio, archivo):
	global cntnd
	cnxn = requests.get(sitio) #cnxn viene de "conexión" sin las vocales xD

	rchv = open(archivo, "a") #rchv viene de "archivo", soy muy original, lo sé
	cntnd = cnxn.text #cntnd viene de "contenido", ok ya vale 
	rchv.write(cntnd) #Guarda el contenido
	rchv.close() #Cierra el archivo

	print("Archivo ", archivo, " creado con exito!")

def buscar(dirc):
	cnxn = requests.get(dirc)
	cntnd = cnxn.text
	os.system("clear")
	print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
	print("Buscar un conjunto de caracteres en el codigo fuente. (Pulsa ENTER para saltar)")
	plbr = input(str(">> "))
	if len(plbr) > 1:
		x = cntnd.find(plbr)
		y = x - 10
		w = x + len(plbr) + 15
		z = cntnd[y:w]
	else:
		print("No se ha introducido ningun dato, saliendo...")
		exit()
	if x < 0:
		print("")
		print("No se han encontrado coincidencias")
	else:
		print("")
		print("Se ha encontrado ", plbr, " en el texto analizado:")	
		print(z)
	print("Deseas buscar otra cadena de caracteres? (s/n)")
	otra = input(">> ")
	if otra == "s":
		buscar(dirc)
