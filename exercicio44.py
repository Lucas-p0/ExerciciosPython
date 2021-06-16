"""Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros"""

preco = float(input('Preço das compras: R$:'))
print("""FORMAS DE PAGAMENTO
[1] à vista dinheiro / cheque
[2] à vista cartão
[3] 2x no cartão 
[4] 3x no cartão""")
formaDePagamento = int(input('Qual a opção?:'))

if formaDePagamento == 1:
    preco = preco - (preco * 0.10)
    print('Sua compra será à vista no dinheiro/cheque, com desconto de 10% o valor ficará: R${:.2f}'.format(preco))
elif formaDePagamento == 2:
    preco = preco - (preco * 0.05)
    print('Sua compra será à vista no cartão, com desconto de 20% o valor ficará: R${:.2f}'.format(preco))
elif formaDePagamento == 3 or 4:
    parcelas = int(input('Quantas vezes no cartão?:'))
    if parcelas == 2:
        print('O preço será :R${}'.format(preco))
    elif parcelas > 3:
        precoComJuros = preco + (preco * 0.20)
        valorDaParcela = precoComJuros / parcelas
        print('Sua compra será parcelada em {} de {} COM JUROS.'.format(parcelas, valorDaParcela))
        print('Sua compra de R${} vai custar R$:{} no final.'.format(preco, precoComJuros))