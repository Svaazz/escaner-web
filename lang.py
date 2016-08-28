
def main(palabra):
	return {
		'cabecera1':"""\
		################ Web Scanner ###############
		Current URL: """,
		'cabecera2':"""
		############################################ """,
		'menu1':"""
		0. Exit.
		1. Search string.
		2. Save webpage on hard drive.
		3. Change URL.
		4. Scan opened ports. (IP Needed)
		5. Open in browser.
	   	############################################
	    """,
	    'nArch':"Type file's name:",
	    'elArch':"The file ",
	    'sCreado':" is being created",
	    'cambUrl':"CHANGE URL.",
	    'saliendo':"Exiting...",
	    'intUrl':"Please type an URL: (http://example.com)",
	    'errUrl':"ERROR: NOT VALID URL.",
	    'arch':"File ",
	    'creado':" succesfully created!",
	    'bCarac':"Search a string in the webpage code. (Press ENTER to skip)",
	    'noDato':"No data introduced, exiting...",
	    'noCoin':"No coincidences were found",
	    'seEncon':"Found ",
	    'enTxt':" in the scanned text:",
	    'bOtra':"Do you want to search another string? (y/n)",
	    'intIp':"Type the IP you want to scan:",
	    'pAb':'Port {}: Opened',
	    'esDes':"Scan from: ",
	    'esHas':"Scan to: ",
	    'errPuer':"ERROR: Port range is from 1 to 1025!",    
	}[palabra]

