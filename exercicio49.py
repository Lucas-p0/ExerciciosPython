'''Exercício Python 049: Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.'''


def tabuada_multiplica(valor):
    for i in range(1, 11):
        soma = valor*i
        print('{} x {} = {}'.format(valor, i, soma))


numero = int(input('digite um numero para ver sua tabuada:'))
tabuada_multiplica(numero)
