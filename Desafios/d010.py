print('Conversor de real para dólar')
real = float(input('Quanto reais você quer converter? '))
dolar = real/4.97
print('Seus R${} valem ${:.2}'.format(real, dolar))
