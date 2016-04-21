	def sumanumnatural(n):
		i=1
		suma=0
	
		while i<=n:
			suma=suma+i
			i=i+1
		print "La suma de los m naturales de 1 hasta ",n, " es",suma

		

	n=input("Ingrese el valor hasta el cual desea ver los numeros naturales: ")
	sumanumnatural(n)