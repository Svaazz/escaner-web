def main(palabra):
	return {
		'cabecera1':"""\
		################ Escaner Web ###############
		URL actual: """,
		'cabecera2':"""
		############################################ """,
		'menu1':"""
		0. Salir.
		1. Buscar cadena de caracteres.
		2. Guardar contenido en el disco.
		3. Cambiar url.
		4. Escanear puertos abiertos. (Necesaria IP)
		5. Abrir en el navegador.
	   	############################################
	    """,
	    'nArch':"Introduce un nombre para el archivo:",
	    'elArch':"El archivo ",
	    'sCreado':" esta siendo creado",
	    'cambUrl':"CAMBIAR URL.",
	    'saliendo':"Saliendo...",
	    'intUrl':"Por favor introduce una URL: (http://ejemplo.com)",
	    'errUrl':"ERROR: URL NO VALIDA.",
	    'arch':"Archivo ",
	    'creado':" creado con exito!",
	    'bCarac':"Buscar un conjunto de caracteres en el codigo fuente. (Pulsa ENTER para saltar)",
	    'noDato':"No se ha introducido ningun dato, saliendo...",
	    'noCoin':"No se han encontrado coincidencias",
	    'seEncon':"Se ha encontrado ",
	    'enTxt':" en el texto analizado:",
	    'bOtra':"Deseas buscar otra cadena de caracteres? (s/n)",
	    'intIp':"Introduce la IP que deseas escanear:",
	    'pAb':'Puerto {}: Abierto',
	    'esDes':"Escanear desde: ",
	    'esHas':"Escanear hasta: ",
	    'errPuer':"ERROR: El rango de puertos va de 1 a 1025!",
	}[palabra]


