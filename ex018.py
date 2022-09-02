# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

mb = float(input('Tamanho do arquivo, em MB: '))
mbps = float(input('Velocidade do link da sua internet, em Mbps: '))
seg = mb / mbps
min = seg / 60

print('Seu arquivo levará {:.2f} minutos para carregar!'.format(min))
