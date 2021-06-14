"""Exercício Python 041: A Confederação Nacional de Natação precisa de um
 programa que leia o ano de nascimento de um atleta e mostre sua categoria,
de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER"""

from datetime import date

anoNascimento = int(input('Digite o ano de nascimento do atleta!:'))
idade = date.today().year - anoNascimento


print('Você tem {} anos de idade categoria:'.format(idade))
if idade < 9:
    print('Mirim')
elif 14 <= idade < 18:
    print('infantil')
elif 19 <= idade < 24:
    print('Júnior')
elif idade > 25:
    print('Master')
