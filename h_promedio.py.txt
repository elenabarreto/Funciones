print "_______________________"
	print "       PROMEDIO         "
	print "_______________________"
	print " "
	print " "
	def promedio(n):
		i=1
		suma=0
	
		while i<=n:
			suma=suma+i
			i=i+1
		promedio=suma/n
		print "El promedio de los naturales de 1 hasta ",n, " es",promedio

	n=input("Ingrese el valor hasta el cual desea ver el promedio de la suma de los numeros naturales: ")
	promedio(n)