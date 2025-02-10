#utilizar la formula cuadratica
# x2 + 5x+ 6
#solicitud de los datos de la ecuacion
number1 = int(input("ingresa el primer numero:"))

number2 = int(input("ingresa el segundo numero:"))

number3 = int(input("ingresa el tercer numero:"))

#resolucion

parte1 = (-number2 + (number2**2  - 4*number1*number3)**0.5) / (2*number1)
parte2 = (-number2 - (number2**2 - 4*number1*number3)**0.5) / (2*number1)

print(parte1)
print(parte2)
