import time
""""Exercício Python 046:
Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício,
indo de 10 até 0, com uma pausa de 1 segundo entre eles."""


'''n = int(input('Digite o valor para contagem:'))
s = 0
print(n)
for i in range(n, 0, -1):
    n = n-1
    time.sleep(1)
    print(n)'''


def contagem_regressiva(valor):
    print(f'Contagem regressiva para {valor}:')
    for i in range(valor, 0, -1):
        valor -= 1
        time.sleep(1) 
        print(valor)


n = int(input('Digite o valor para contagem: '))
contagem_regressiva(n)
