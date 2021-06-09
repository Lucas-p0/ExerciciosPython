"""Exercício Python 039: Faça um programa que leia o ano de nascimento de um jovem e informe,
de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
se é a hora exata de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo."""
from datetime import date

#variaveis
anoNascimento = int(input('Ano de nascimento:'))
dataAtual = date.today().year
idade =  dataAtual - anoNascimento
anoAlistamento = idade - 18



print('Quem nasceu em {} e tem {} anos em {}.'.format(anoNascimento, idade, dataAtual))
if idade < 18:
    print("Ainda faltam {} anos para o alistamento.".format(anoAlistamento))
elif idade > 18:
    print("Você deveria ter se alistado há {} anos .".format(anoAlistamento))
else:
    print("Você tem que se alistar IMEDIATAMENTE!")