# -*-encoding:utf-8 -*-
print("-------------")
print("Ejercicio 1-M")
print("-------------\n")

def ubicar(x):
	L1 = 10
	L2 = 50
	if x >= L1 and x <= L2:
		return "adentro"
	elif x < L1:
		return "a derecha"
	else:
		return "a izquierda"

x = input("Ingresar un número: ")

salida = ubicar(x)

print("El número ingresado está %s del rango dado." % (salida))
