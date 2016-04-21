print "Suma de Impares"
print " "
def sumanatimpar(n):
	i=1
	suma=0

	while i<=n:
		if i%2!=0:
			suma=suma+i
		i=i+1
	print "La suma de los n naturales impares de 1 hasta ",n, " es",suma

#n=input("Ingrese el valor hasta el cual desea ver los numeros naturales: ")
#sumanatimpar(n)