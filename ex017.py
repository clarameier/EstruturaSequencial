# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00. Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# a) comprar apenas latas de 18 litros;
# b) comprar apenas galões de 3,6 litros;
# c) misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

#programa
import math

area = float(input('Diga, em m², o tamanho da área a ser pintada: '))

tinta = area / 6

#LATAS
latas = tinta / 18
arred = math.ceil(latas)
total_latas = arred * 80.00

#GALÃO
galao = tinta / 3.6
arreg = math.ceil(galao)
total_galao = arreg * 25.00

# a)
print('Se escolher comprar latas, você precisará de {} litros.'.format(tinta))
print('Ou seja, em uma lata vem 18 litros, e por isso, você precisará de apenas {} lata(s).'.format(arred))
print('Logo, seu total será de {} reais.'.format(total_latas))

#b)
print('Porém, se você escolher comprar em galão, vai estar precisando ainda de {} litros.'.format(tinta))
print('Então, como um galão vem 3,6 litros, você precisará de apenas {} galão(ões).'.format(arreg))
print('Logo, seu total será de {} reais.'.format(total_galao))
