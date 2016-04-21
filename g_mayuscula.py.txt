	print "_______________________"
	print "  Mayusculas con upper "
	print "_______________________"
	print " "
	print " "
	def mayuscula(s):
		if s.upper()==True:
			print "El caracter ingresado es mayuscula"
		else:
			print "El caracter ingresado en mayuscula es: ",s.upper()
	s=raw_input("Ingrese un caracter => ")
	mayuscula(s)