"""Exercício Python 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado."""

valorDaCasa = float(input('Qual o valor da casa?:'))
salarioComprados = float(input('Qual o Sálario do comprador?:'))
anosFinanciamento = int(input('Quantos anos de financiamento?:'))
calculoSalario = salarioComprados * 30 / 100
prestacao = valorDaCasa / (anosFinanciamento * 12)


print('Para pagar {:.2f} em {} a prestação será de {:.2f}.'.format(valorDaCasa, anosFinanciamento, prestacao))
if prestacao <= calculoSalario:
    print('Empréstimo aprovado')

else:print('Empréstimo negado')