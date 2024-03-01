from math import sqrt, pow
n1 = int(input('Digite o valor do cateto oposto: '))
cat_o = pow(n1, 2)
n2 = int(input('Digite o valor do cateto ajacente: '))
cat_a = pow(n2, 2)
h = sqrt(cat_o + cat_a)
print('A hipotenusa é igual a: {}'.format(h))