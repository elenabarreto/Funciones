def numparoimpar(m):
	if m%2==0:
		i=1
		print "Numeros pares de 1 hasta ",m
		while i<=m:
			if i%2==0:
				print "=> ",i
			i=i+1
	else:
		i=1
		print "Numeros impares de 1 hasta ",m
		while i<=m:
			print "=> ", i


			i=i+2
m=input("Ingrese el valor hasta el cual desea ver los numeros naturales: ")
numparoimpar(m)