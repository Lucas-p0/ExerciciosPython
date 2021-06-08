"""Exercício Python 033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor."""
primeiro = int(input('Digite o primeiro número:'))
segundo = int(input('Digite o segundo número:'))
terceiro = int(input('Digite o terceiro número:'))


#Achando o maior número
maior = primeiro

print('-==-'*10)

if segundo > maior:
    maior=segundo
if terceiro > maior:
    maior=terceiro
print('O maior número é: {}'.format(maior))



#Achando o menor número
menor = primeiro


if segundo < menor:
    menor=segundo
if terceiro < menor:
    menor=terceiro
print('O menor número é: {}'.format(menor))
