# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius. C = 5 * ((F-32) / 9).

n1 = float(input('Diga uma temperatura em Fahrenheit: '))
n2 = n1 - 32
n3 = 5 * n2 / 9
print('{}° Fahrenheits, em graus Celsius são {}°!'.format(n1, n3))