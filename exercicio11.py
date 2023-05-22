'''Exercício Python 011: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
'''
largura_da_parede = float(input('Largura da parede:'))
altura_da_parede = float(input('Altura da parede:'))
area_da_parede = largura_da_parede*altura_da_parede
quantidade_de_tinta = area_da_parede/2

print('Sua parede tem a dimensão de {} x {} e sua área é de {}m².'
      .format(largura_da_parede, altura_da_parede, area_da_parede))
print('Para pinta essa parede, você precisará de {:.2f}l de tinta.'
      .format(quantidade_de_tinta))
