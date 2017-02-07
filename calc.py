#!/usr/bin/python3
import sys

NUM_VALORES= 4 #constantes definirlas con mayusculas

if len(sys.argv) != NUM_VALORES:
	sys.exit("Usage: python3 calc.py operacion operando1 operando2")


funcion= sys.argv[1]
try:
	op1 = float(sys.argv[2])
	op2 = float(sys.argv[3])
except ValueError:
	sys.exit("Los operandos han de ser floats. Gracias")


if funcion == 'suma':
	print(op1 + op2)
elif funcion == 'resta':
	print(op1 - op2)
elif funcion == 'div':
	try:
		print(op1/op2)
	except ZeroDivisionError:
		sys.exit("No se dividir por 0")
elif funcion == 'mult':
	print(op1 * op2)
else:
	print("Operador incorrecto")


