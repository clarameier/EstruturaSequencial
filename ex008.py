# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

hora = float(input('Quanto você ganha por hora? '))
mes = int(input('Por quantas horas você trabalhou este mês? '))
total = hora * mes
print('Este mês seu salário foi de {} reais.'.format(total))