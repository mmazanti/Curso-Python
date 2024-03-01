from math import radians, sin, cos, tan
n = int(input('Digite um número '))
a = radians(n)
s = sin(a)
c = cos(a)
t = tan(a)
print('A medida é: {}°. \nSeu seno é: {} \nSeu consseno é: {} \nSua tangente é: {}'.format(n, s, c, t))