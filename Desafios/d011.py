print('Cálculo de área para pintor')
largura = float(input('Qual a largura da parede? '))
altura = float(input('Qual a altura da parede? '))
area = largura*altura
tinta = area/2
print('A parede mede {}x{}m, sua área é de {}m². Para pinta-la você vai precisar de {}l de tinta.'.format(largura, altura, area, tinta))
