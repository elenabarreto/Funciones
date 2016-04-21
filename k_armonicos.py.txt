print "Numeros Armonicos"
	print""
	def numarmonico(n):
		i=0
		suma=0
	
		while i<=n:
			i=i+1
			suma=suma+(1/i)
		
		print "La suma de numeros armonicos Hn=1+1/2...+1/n es ",suma

	n=input("Ingrese el valor hasta el que desea calcular la formula de numeros armonicos: ")
	numarmonico(n)