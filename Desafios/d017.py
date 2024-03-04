from math import hypot
cateto_oposto = float(input('Digite o valor do cateto oposto: '))
cateto_adjacente = float(input('Digite o valor do cateto ajacente: '))
hipotenusa = hypot(cateto_oposto, cateto_adjacente)
print('A hipotenusa é igual a: {:.2f}'.format(hipotenusa))