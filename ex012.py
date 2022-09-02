# Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

altura = float(input('Digite o valor da sua altura: '))
p1 = 72.7 * altura
pi = p1 - 58
print('Sendo a sua altura de {}cm, então o seu peso ideal deverá ser de aproximadamente {}kg!'.format(altura, pi))