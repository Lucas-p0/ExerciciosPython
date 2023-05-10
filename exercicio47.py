import matplotlib.pyplot as plt
from random import randrange, seed

seed(10)
randrange(0, 11)

notas_de_matematica = []

for notas in range(8):
    notas_de_matematica.append(randrange(0, 11))

print(notas_de_matematica)
len(notas_de_matematica)


x = list(range(1, 9))
y = notas_de_matematica
plt.plot(x, y, marker='o')
plt.title('Notas de Matemática')
plt.xlabel('Provas')
plt.ylabel('Notas')
plt.show()
