def factorialnatural(x):
		i=1
		factorial=1
		n=x
		while i<n:
			factorial=factorial*(x)
			x=x-1
			i=i+1

		print "El resultado de calcular el factorial de ",x," es => ",factorial
		

	x=input("Ingrese el numero natural del cual desea calcular el factorial: ")	
	factorialnatural(x)