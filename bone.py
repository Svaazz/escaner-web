#By Svaazz

import requests
import os
import socket
import lang

cntnd = ""
def conectar(sitio, archivo):
	global cntnd
	cnxn = requests.get(sitio) #cnxn viene de "conexión" sin las vocales xD

	if archivo.endswith('.html'):
		pass
	else:
		archivo += ".html"
	rchv = open(archivo, "a") #rchv viene de "archivo", soy muy original, lo sé
	cntnd = cnxn.text #cntnd viene de "contenido", ok ya vale 
	rchv.write(cntnd) #Guarda el contenido
	rchv.close() #Cierra el archivo

	print(lang.main('arch'), archivo, lang.main('creado'))

def buscar(dirc):
	cnxn = requests.get(dirc)
	cntnd = cnxn.text
	limpiar()
	print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
	print(lang.main('bCarac'))
	plbr = input(str(">> "))
	if len(plbr) > 1:
		x = cntnd.find(plbr)
		y = x - 10
		w = x + len(plbr) + 15
		z = cntnd[y:w]
	else:
		print(lang.main('noDato'))
		exit()
	if x < 0:
		print("")
		print(lang.main('noCoin'))
	else:
		print("")
		print(lang.main('seEncon'), plbr, lang.main('enTxt'))	
		print(z)
	print(lang.main('bOtra'))
	otra = input(">> ")
	if otra == "s" or otra == "y":
		buscar(dirc)

def puertos(dirc):
	limpiar()
	print(lang.main('intIp')) 
	dIP = input('>> ')
	print(lang.main('esDes'))
	x = input(">> ")
	print(lang.main('esHas'))
	y = input(">> ")
	limpiar()
	x = int(x)
	y = int(y)
	if x < 1 or y > 1025 or x > 1024 or y < 2:
		print(lang.main('errPuer'))
		puertos(dirc)
	else:
		for port in range (x, y):

			sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

			rslt = sock.connect_ex((dIP,port))

			if rslt == 0:

				print(lang.main('pAb').format(port))

	sock.close()

def navegador(dirc):
	if os.name == "nt":
		instruccion = "start firefox " + dirc
	else:
		instruccion = "firefox " + dirc

	try:
		os.system(instruccion)
		
	except valorError:
		print("ERROR: ", valorError)


def limpiar():
	if os.name == "nt":
		os.system("cls")
	else:
		os.system("clear")