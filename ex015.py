# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# a) salário bruto.
# b) quanto pagou ao INSS.
# c) quanto pagou ao sindicato.
# d) o salário líquido.
# e) calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$
# Obs.: Salário Bruto - Descontos = Salário Líquido. 

# programa
hora = float(input('Quanto você recebe por hora? '))
mes = int(input('Por quantas horas você trabalhou este mês? '))

# a)
bruto = hora * mes
print('Seu salário bruto, por mês, é de {} reais.'.format(bruto))

# b)
inss = bruto * 0.08
print('Seu salário será descontado no valor de {} reais, para o INSS.'.format(inss))

# c)
sindicato = bruto * 0.05
print('Seu salário será descontado no valor de {} reais, para o sindicato.'.format(sindicato))

# d) ; e)
ir = bruto * 0.11
liquido = bruto - inss - sindicato - ir
print('Seu salário será descontado no valor de {} reais, para o imposto de renda.'.format(ir))
print('Portanto, seu salário liquído final será de {} reais.'.format(liquido))
