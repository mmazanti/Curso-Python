n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
som = n1 + n2
sub = n1 - n2
mul = n1 * n2
div = n1 / n2
res = n1 // n2
exp = n1 ** n2
print('A soma vale {} \nA subtração é {} \nO produto é {} \nA divisão é {:.3f} \nO resto é {} \nA exponenciação é {}'.format(som, sub, mul, div, res, exp))