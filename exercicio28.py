import random
from time import sleep

print('-=-'*20)
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar... ')
print('-=-'*20)



n1 = random.randrange(0, 5)
n2 = int(input('Digite um numero:'))
print('PROCESSANDO...')
sleep(3)

if(n1) == n2: {
    print('NOSSA VOCÊ É UM VIDENTE?')
}
else:{
    print('BURRO! O numero foi:{}'.format(n1))
}
