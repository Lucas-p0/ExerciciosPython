'''Exercício Python 018: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
'''
import math
n = float(input('Digite o ângulo que você deseja:'))
print('Seno {:.2f}'.format(math.sin(math.radians(n))))
print('Cossenno {:.2f}'.format(math.cos(math.radians(n))))
print('Tangente {:.2f}'.format(math.tan(math.radians(n))))
