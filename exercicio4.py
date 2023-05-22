'''
Exercício Python 004: Faça um programa que leia algo pelo teclado e 
mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
'''

n = int(input('Digite um número:'))
print('O dobro de {} é {}!'.format(n, (n*2)))
print('O triplo de {} é {}!'.format(n, (n*3)))
print('A raiz quadrada de {} é {:.2f}!'.format(n, (n**(1/2))))


print('O nurmero é {} anterior é {} e o proximo {}'.format(n, (n-1), (n+1)))
