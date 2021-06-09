"""Exercício Python 039: Faça um programa que leia o ano de nascimento de um jovem e informe,
de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
se é a hora exata de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo."""
from datetime import date

#variaveis
anoNascimento = int(input('Ano de nascimento:'))
dataAtual = date.today().year
idade =  dataAtual - anoNascimento




print('Quem nasceu em {} e tem {} anos em {}.'.format(anoNascimento, idade, dataAtual))
if idade < 18:
    calculoAlistamento = 18 - idade
    anoDoAlistamento = dataAtual + calculoAlistamento
    print("Ainda faltam {} anos para o alistamento, você se alistará em {} .".format(calculoAlistamento, anoDoAlistamento))


elif idade > 18:
    calculoAlistamento = idade - 18
    anoDoAlistamento = dataAtual - calculoAlistamento
    print("Você deveria ter se alistado há {} anos, em {} .".format(calculoAlistamento, anoDoAlistamento))
else:
    print("Você tem que se alistar IMEDIATAMENTE!")