velocidade = float(input('Qual sua velocidade atual do carro? '))
limite = 80.0
if velocidade > limite:
    print('MULTADO! Sua multa é de R$ {:.2f}'.format((velocidade-limite)*7))
print('Tenha um bom dia! Dirija com segurança e respeite as leis de trânsito!')