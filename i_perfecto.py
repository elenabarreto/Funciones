	
	print "_____________________________________________________"
	print "      Numeros perfectos, deficientes y abundante     "
	print "______________________________________________________"
	print " "
	print " "
	def perfectos(k):
		i=1
		suma=0
		
		while i<=k:
			if k%i==0:
				suma=suma+i
				print  i,"es divisor de ",k
			if suma==k:
				print "El numero ",k,"ingresado es PERFECTO"
			elif suma<k:
				print "El numero ",k,"ingresado es DEFICIENTE" 
			elif suma>k:
				print "El numero ",k,"ingresado es ABUNDANTE" 
			i=i+1


	k=input("Ingrese el valor del que desea evaluar si es perfecto, deficiente o abundante =>  ")
	perfectos(k)
