'''Exercício Python 015: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
'''
dias_alugados = float(input('Quantos dias alugados?:'))
quilometragem = float(input('Quantos Km rodados?:'))

total = (dias_alugados*60)+(quilometragem*0.15)

print('O total a pagae é de R${:.2f}'.format(total))
