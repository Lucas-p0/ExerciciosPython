temperatura_c = float(input('Digite a temperatura em °c:'))
temperatura_f = (temperatura_c*9/5)+32
temperatura_k = temperatura_c+273.15
print('A temperatura de {:.2f}°C corresponde a {:.2f}°F!'
      .format(temperatura_c, temperatura_f))
print('A temperatura de {:.2f}°C correnponde a {:.2f} k!'
      .format(temperatura_c, temperatura_k))
