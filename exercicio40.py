"""Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO"""

num1 = float(input('Digite a primeira nota:'))
num2 = float(input('Digite a segunda nota:'))
media = (num1 + num2) / 2
print('Com as notas {:.2f} e {:.2f}, a média {:.2f}.'.format(num1, num2, media))
if media >= 7:
    print('Aluno aprovado! ')
elif 6.9 >= media > 5:
    print('Aluno de recuperação! ')
elif media < 5:
    print('Aluno reprovado! ')