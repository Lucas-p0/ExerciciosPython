"""Exercício Python 031:

Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas."""

distancia = float(input('Digite a distância desejada em km para sua viagem:'))
print('Você deseja cotar uma viagem de {} km.'.format(distancia))

if (distancia) <= 200:
    preco = distancia*0.50
else:
    preco = distancia*0.45
print('O preço da passagem será de R${:.2f}'.format(preco))


