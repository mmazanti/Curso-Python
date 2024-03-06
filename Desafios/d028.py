from random import randint
from time import sleep
computador = randint(0, 5) #faz o computador "PENSAR" em um número
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*20)
jogador = int(input('Em qual número eu pensei? ')) #Jogador tenta adivinhar o número.
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('PARABÉNS, você venceu! O número era {}'.format(computador))
else:
    print('VOCÊ PERDEU! Eu pensei no número {} e não no {}'.format(computador, jogador))
