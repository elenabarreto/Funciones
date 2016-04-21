def detector_suma(a,b,c):
	if (num_1 == num_2 + num_3) or (num_2 == num_3 + num_1) or (num_3 == num_1 + num_2):
		band = True
	else:
		band = False
	return band
#PROGRAMA
num_1 = int (input("Ingrese el primer numero"))
num_2 = int (input("Ingrese el segundo numero")) 
num_3 = int (input("Ingrese el tercer numero"))
SIno = detector_suma(num_1,num_2,num_3)
if SIno:
	print "Uno de los numeros es suma de los otros!!"
else:
	print "Ninguno de los numeros es suma de los otros"