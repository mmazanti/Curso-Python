from math import radians, sin, cos, tan
angulo = float(input('Digite um número '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('A medida é: {}°. \nSeu seno é: {:.2f} \nSeu consseno é: {:.2f} \nSua tangente é: {:.2f}'.format(angulo, seno, cosseno, tangente))