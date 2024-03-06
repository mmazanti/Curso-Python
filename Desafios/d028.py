from random import randint
palpite = int(input('Em qual número eu to pensando de 0 a 5? '))
numero = randint(0, 5)
if palpite == numero:
    print('Você acertou! O número era {}'.format(numero))
else:
    print('Você perdeu! O número era {}'.format(numero))
