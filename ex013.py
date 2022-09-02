# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

# programa
altura = float(input('Digite o valor da sua altura: '))
ph1 = 72.7 * altura
ph2 = ph1 - 58
pm1 = 62.1 * altura
pm2 = pm1 - 44.7

# homens
print('Como homem, dado a sua altura de {}cm, o seu peso ideal deverá ser de aproximadamente {}kg.'.format(altura, ph2))

# mulheres
print('Como mulher, dado a sua altura de {}cm, o seu peso ideal deverá ser de aproximadamente {}kg.'.format(altura, pm2))
