def exponentenatural(j,h):
	i=1
	exponente=1
	while i<=h:
		exponente=exponente*j
		i=i+1

	print "El resultado de hacer ",j, "**",h," es => ",exponente
	

j=input("Ingrese el numero natural base: ")	
h=input("Ingrese el numero natural exponente: ")
exponentenatural(j,h)