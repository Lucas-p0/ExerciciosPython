'''Exercício Python 027: Faça um programa que leia o nome completo de uma pessoa, 
mostrando em seguida o primeiro e o último nome separadamente.
'''
n = str(input('Qual o seu nome completo?:')).strip()
nome = n.split()
print('Seu primeiro nome é :{}'.format(nome[0]))
print('Seu ultimo nome é : {}'.format(nome[len(nome)-1]))
print('Seu nome completo tem: {} palavras'.format(len(nome)))
