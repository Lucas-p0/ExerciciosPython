'''Exercício Python 047: Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
 '''
import time


def contagem_par(valor):
    for i in range(0, 50):
        valor += 1
        time.sleep(1)
        if valor % 2 == 0:
            print(valor)


n = int(input('Digite o valor para contagem: '))
contagem_par(n)
