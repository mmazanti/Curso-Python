ano = int(input('Digite um ano: '))
bissexto = ano % 4
if bissexto == 0:
    print('O ano {} é bissexto'.format(ano))
else:
    print('O ano {} não é bissexto'.format(ano))