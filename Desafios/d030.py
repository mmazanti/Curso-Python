numero = int(input('Digite um número: '))
par_impar = numero % 2
if par_impar == 0:
    print('O número {} é par'.format(numero))
else:
    print('O número {} é impar'.format(numero))