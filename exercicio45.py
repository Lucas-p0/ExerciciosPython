"""Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô com você."""
from random import randint
from time import sleep

print("""Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA""")

itens = ('Pedra', 'Papel', 'Tesoura')
jogador = int(input('Qual é a sua jogada?'))
computador = randint(0, 2)


print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')

print('-='*11)
print('O computador escolheu {}'.format(itens[computador]))
print('O jogador escolheu {}'.format(itens[jogador]))
print('-='*11)

if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
else:
    print('\33 JOGADA INVÁLIDA')