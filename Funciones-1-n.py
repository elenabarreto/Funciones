def aPies(medida):
	pul = aPulgadas(medida)
	salida = (pul/12)
	return salida

def aPulgadas(medida):
	salida = (medida*39.37)
	return salida

"""print("==================================")
print("	Conversor de medidas")
print("==================================\n")
medida = input("Ingrese una medida en metros: ")
pies = aPies(medida)
pulgadas = aPulgadas(medida)

print("\nLa medida en pulgadas es: %f y en pies es: %f\n" % (pulgadas,pies))"""
