# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

area = float(input('Diga, em m², o tamanho da área a ser pintada: '))

tinta = area / 3
print('Você precisará de {} litros por cada 3 metros'.format(tinta))

latas = tinta / 18
arred = round(latas + 1)
print('Ou seja, em uma lata vem 18 litros, e por isso, você precisará de apenas {} lata(s).'.format(arred))

total = arred * 80.00
print('Logo, seu total será de {} reais.'.format(total))