'''Exercício Python 026: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
'''
frase = str(input('Digite uma frase:')).upper().strip()
print('A letra (A) aparece {} vezes na frase'.format(frase.count("A")))
print('Em qual posição a letra (A) fora encontrado primeiro na posição:{}'.format(
    frase.find('A')+1))
print('Em qual posição a letra (A) fora encontrada pela ultima vez?:{}'.format(
    frase.rfind('A')+1))
