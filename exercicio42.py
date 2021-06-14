"""Exercício Python 042: Refaça o DESAFIO 035 dos triângulos,
   acrescentando o recurso de mostrar que
   tipo de triângulo será formado:

- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes"""


print('-='*20)
print('Analisador de Triângulos')
print('-='*20)

primeiro = float(input('Primeiro segmento:'))
segundo = float(input('Segundo segmento:'))
terceiro = float(input('Terceiro segmento:'))

if primeiro + segundo > terceiro and segundo + terceiro >primeiro and terceiro + primeiro > segundo:
    print('É um triângulo')
    if primeiro == segundo == terceiro:
        print('EQUILÁTERO')
    elif primeiro != segundo != terceiro != primeiro:
        print('ESCALENO')
    else:
        print('ISÓRCELES')

else:
    print('Não é nada, lixo!')