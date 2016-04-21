
print " "
print " "

print "__________________________________________"
print "*-       Division de Billetes             -*"
print "___________________________________________"
print " "
print " "
print " "

def billetes(n):
	while n!=0:

		if n>=100:
			cant100=n/100
			n=n%100
			print "Cantidad de billetes de cien: ",cant100
		elif n>=50: 
			cant50=n/50
			n=n%50
			print "Cantidad de billetes de cincuenta: ",cant50
		elif n>=20:
			cant20=n/20
			n=n%20
			print "Cantidad de billetes de veite: ",cant20
		elif n>=10:
			cant10=n/10
			n=n%10
			print "Cantidad de billetes de diez: ",cant10
		elif n>=5:
			cant5=n/5
			n=n%5
			print "Cantidad de billetes de cinco: ",cant5
		elif n>=2:
			cant2=n/2
			n=n%2
			print "Cantidad de billetes de dos: ",cant2
		elif n>=1:
			cant1=n/1
			n=n%1
			print "Cantidad de monedas de uno: ",cant1

num  = input("Ingrese monto: ")
billetes(num)
