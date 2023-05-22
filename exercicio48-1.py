'''Exercício Python 048: Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.'''
# 1 - Calcular os multiplos de 3 e armazenar em uma lista;
# 2 - Varrer a lista contar a quantiade de numeros e calcular o montante;

valor = 1


def contador_multiplo_tres(valor: int):
    lista_multiplo_tres = []

    for i in range(1, 501, 2):
        if i % 3 == 0:
            lista_multiplo_tres.append(i)
        quantidade = len(lista_multiplo_tres)

        soma_de_lista = 0
        for lista in lista_multiplo_tres:
            soma_de_lista += lista

    # print(quantidade)
    # print(lista_multiplo_tres)
    print(
        f'A quantidad de multiplos de 3 de 0 até 500 é de {len(lista_multiplo_tres)} e a soma desses numeros é {soma_de_lista}')


contador_multiplo_tres(0)
