'''Exercício Python 024: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
'''
cid = str(input('Em que cidade você nasceu?:')).upper()
cid2 = str(cid.split())
print('SANTO' in cid2)
print('Você mora em uma cidade que começa com a palavra:{}'.format(cid2))

if (cid2) == str('SANTO'):
    {
        print('verdadeiro')
    }
else:
    {
        print('falso')
    }
