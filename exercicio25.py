'''Exercício Python 025: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
'''
nome = str(input('Qual é seu nome completo?:')).upper()
print('Seu nome tem Silva?:{}'.format('SILVA' in nome.split()))
