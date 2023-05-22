'''Exercício Python 023: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
'''
num = int(input('Irforme o número:'))
u = num//1 % 10
d = num//10 % 10
c = num//100 % 10
m = num//1000 % 10

print('Analisando o numero: {}'.format(num))


if (u) == 0:
    {
        print('Não tem unidade em: {}'.format(num))
    }
else:
    {
        print('A Unidade do número é: {}'.format(u))
    }
if (d) == 0:
    {
        print('Não tem dezena em: {}'.format(num))
    }
else:
    {
        print('A dezena do número é: {}'.format(d))
    }

if (c) == 0:
    {
        print('Não tem centena em: {}'.format(num))
    }
else:
    {
        print('A centena do número é: {}'.format(c))
    }

if (m) == 0:
    {
        print('Não tem milhar em: {}'.format(num))
    }
else:
    {
        print('A milhar do número é: {}'.format(m))
    }
