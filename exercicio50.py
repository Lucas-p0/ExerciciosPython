'''Exercício Python 050: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.'''

numeros = input('Digite 6 numeros separados: ')


def soma_pares(numeros: list):
    lista_numeros_pares = []

    for i in range(0, 6):
        if numeros % 2 == 0:
            lista_numeros_pares.append(numeros)
    soma_de_lista = 0
    for lista in lista_numeros_pares:
        soma_de_lista += lista
    print(soma_de_lista)


# soma_pares(numeros)

print(soma_pares(numeros))
