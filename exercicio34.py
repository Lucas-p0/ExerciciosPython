"""Exercício Python 034: Escreva um programa que pergunte o salário de um
funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%"""

salario = float(input('Digite seu salário R$:'))

if salario > 1250 :
    aumento = salario * 0.10
if salario <=1250:
    aumento = salario * 0.15
salarioAumento = aumento+salario
print('Quem ganhava {} passa a ganhar {}'.format(salario, salarioAumento))