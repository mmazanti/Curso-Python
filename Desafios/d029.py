velocidade = float(input('Qual sua velocidade em Km/h? '))
limite = 80.0
if velocidade > limite:
    print('MULTADO! Sua multa é de R$ {:.2f}'.format((velocidade-limite)*7))
else:
    print('Respeite as leis de transito.')