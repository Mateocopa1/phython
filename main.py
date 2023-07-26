num = 1 #esta es una variable de tipo entero o integer (int)
name = "Mateo Valencia Sanchez" #esta es una variable de tipo cadena o string (str)
div = 1.7 # esta es una variable de tipo decimal o float
bol = True # esta es una variable de tipo booleano
"""
los float mínima precisión es 2.2250738585072014e-308 y la máxima 1.7976931348623157e+308,
los int = no tienen limite Como hemos discutido anteriormente, no hay límite o valor máximo de
un número entero en Python 3, pero hay un límite para el número entero en Python 2, después
del cual el tipo de datos de la variable cambia a un tipo de datos largo. Podemos obtener el
valor entero máximo en Python 2 usando sys.maxint, igual a 2 31 - 1.
creditos www.delftstack.com/es/howto/python/python-max-int/
creditos ellibrodepython.com/float-python
"""
print('ingresa tu edad ')
age = int(input())
print('ingresa tu nombre ')
nombre = input()
str(age)
print(f'tu nombre es {nombre} y tu edad es {age}')

print('ingresa el numero a calcular')
n = int(input())
valor = n * (n+1)
print(f'el valor de tu operacion es {valor}')