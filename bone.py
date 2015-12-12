#By Svaazz

import requests
import os
import socket
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

def puertos(dirc):
	os.system("clear")
	print("Introduce la IP que deseas escanear:") 
	dIP = input('>> ')
	"""print("Escanear desde: ")
	x = input(">> ")
	print("Escanear hasta: ")
	y = input(">> ")
	os.system("clear")
	x = int(x)
	y = int(y)
	if x < 1 or y > 1025 or x > 1024 or y < 2:
		print("ERROR: El rango de puertos va de 1 a 1025!")
		puertos(dirc)
	else:"""
	for port in range (x, y):

		sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

		rslt = sock.connect_ex((dIP,port))

		if rslt == 0:

			print('Puerto {}: Abierto'.format(port))

	sock.close()
