'''Exercício Python 007: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.'''
n = float(input('Digite a primeira nota!:'))
n2 = float(input('Digite a segunda nota!:'))
soma = (n+n2)/2
print('A média total do aluno é:{:2f}'.format(soma))
