"""Exercício Python 041: A Confederação Nacional de Natação precisa de um
 programa que leia o ano de nascimento de um atleta e mostre sua categoria,
de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER"""
anoNascimento = int(input('Digite o ano de nascimento do atleta!:'))
if anoNascimento < 9:
    print('Mirim')
elif 14 <= anoNascimento < 19:
    print('infantil')