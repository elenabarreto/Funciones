	print "_______________________"
	print " SUPERFICIE DE UN CONO "
	print "_______________________"
	print " "
	print " "
	def supcono(g,h,r):
		arealateral=3.14*r*g
		areatotal=arealateral+(3.14*(r**2))
		print "El area lateral del cono es: ",arealateral
		print "El area total del cono es: ",areatotal
		

	g=input("Ingrese la generatriz del cono: ")
	h=input("Ingrese la altura del cono: ")	
	r=input("Ingrese el radio de la base: ")		
	supcono(g,h,r) 