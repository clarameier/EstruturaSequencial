# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

n1 = float(input('Digite a sua nota 1: '))
n2 = float(input('Digite a sua nota 2: '))
n3 = float(input('Digite a sua nota 3: '))
n4 = float(input('Digite a sua nota 4: '))
s = n1 + n2 + n3 + n4
d = s / 4
print('A sua média escolar foi {}!'. format(d))