distancia = float(input('Qual a distância da viagem em km? '))
if distancia <= 200.0:
    print('Sua passagem custa R$ {:.2f}'.format(distancia*0.5))
else:
    print('Sua passagem custa R$ {:.2f}'.format(distancia*0.45))