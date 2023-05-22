'''Exercício Python 013: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
'''
preco = float(input('Qual o preço do produto? R$:'))
desconto = float(input('Qual a porcentagem do desconto? %:'))
novo_preco = preco-(preco*desconto/100)

print('O Valor do item é {}, com o desconto de {:.2f} ficará {:.2f}'
      .format(preco, desconto, novo_preco))
