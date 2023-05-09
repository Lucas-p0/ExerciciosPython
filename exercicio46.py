from pickle import TRUE


idades = [17, 18, 19, 15, 14, 22, 23, 10, 25]


maiores_de_idade = [x for x in idades if x >= 18]
menores_de_idade = [x for x in idades if x < 18]
print(maiores_de_idade)
print(menores_de_idade)


def verifica_se_pode_dirigir(idade):
    if idade >= 18:
        print(f'{idade} anos de idade, TEM permissão para dirigir')
    else:
        print(f'{idade} anos de idade, NÃO tem permissão para dirigir')


for idade in maiores_de_idade:
    verifica_se_pode_dirigir(idade)
for idade in menores_de_idade:
    verifica_se_pode_dirigir(idade)
