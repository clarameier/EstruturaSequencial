# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# a) o produto do dobro do primeiro com metade do segundo.
# b) a soma do triplo do primeiro com o terceiro.
# c) o terceiro elevado ao cubo.

#programa
n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))
n3 = float(input('Por fim, digite um número real: '))

# a)
x = 2 * n1
y = n2 / 2
a = x * y
print('O cálculo do produto do dobro do primeiro com metade do segundo é {}.'. format(a))

# b)
w = n1 * 3
b = w + n3
print('O cálculo da soma do triplo do primeiro com o terceiro é {}'.format(b))

# c)
c = n3 * n3 * n3
print('O cálculo do terceiro elevado ao cubo é {}'.format(c))