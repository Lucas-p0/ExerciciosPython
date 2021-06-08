velocidade = float(input('Qual a sua velocidade?'))
valorMulta=(velocidade-80)*7

if(velocidade) <= 80:{

    print('Tenha um bom dia, dirija com segurança!')
}
else:{
    print('Ta todo errado, toma aqui sua multa: R${:.2f}'.format(valorMulta))
}
