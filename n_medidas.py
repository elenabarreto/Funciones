	print "_______________________"
	print " CONVERSION DE MEDIDAS  "
	print "_______________________"
	print " "
	print " "
	def medidas(mts):
		pulgadas=mts*39.37
		pies=(pulgadas/12)
		print mts," en pulgada es => ",pulgadas
		print mts, "en pies es  => ",pies
		

	mts=input("Ingrese el valor en mts que desea pasar a pulgadas y pies  => ")
			
    medidas(mts) 