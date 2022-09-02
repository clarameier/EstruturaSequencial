# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

n1 = float(input('Diga uma temperatura em Celsius: '))
n2 = 9 / 5 * n1
n3 = n2 + 32
print('{}° Celsius, em Fahrenheits são {}°!'.format(n1, n3))