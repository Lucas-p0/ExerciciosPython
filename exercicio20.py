import random
n1 = input('Primeiro aluno:')
n2 = input('Segundo aluno:')
n3 = input('Terceiro aluno:')
n4 = input('Quanto aluno:')
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('A ordem de apresentação será:')
print(lista)
