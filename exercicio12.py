'''Exercício Python 012: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
'''
preco = float(input('Qual o preço do produto? R$:'))
desconto = float(input('Qual a porcentagem do desconto? %:'))
novo_preco = preco-(preco*desconto/100)
print('O Valor do item é {}, com o desconto de {:.2f} ficará {:.2f}'
      .format(preco, desconto, novo_preco))
