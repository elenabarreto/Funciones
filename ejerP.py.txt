def decomp_digit(a):
	acum = 0
	while (a % 10) != 0:
		acum = acum + a % 10
		a = a // 10
	return acum

num_usu = input ("Ingrese un numero: ")
print "la suma de los digitos del numero es: ", decomp_digit(num_usu)