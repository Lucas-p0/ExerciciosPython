dias_alugados = float(input('Quantos dias alugados?:'))
quilometragem = float(input('Quantos Km rodados?:'))

total = (dias_alugados*60)+(quilometragem*0.15)

print('O total a pagae é de R${:.2f}'.format(total))
