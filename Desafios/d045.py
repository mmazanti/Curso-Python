from random import choice
from time import sleep
jogador = str(input(
    '''VAMOS JOGAR?
    Pedra, Papel ou Tesoura, qual você quer?
    ==>'''
)).upper().strip()
jokenpô = ["Pedra", "Papel", "Tesoura"]
computador = choice(jokenpô).upper().strip()
print('JO...')
sleep(1)
print('KEN...')
sleep(1)
print('PO!')
if jogador == 'PEDRA' and computador == 'TESOURA' or jogador == 'PAPEL' and computador == 'PEDRA' or jogador == 'TESOURA' and computador == 'PAPEL':
    print(f'{jogador} vence {computador}. Você venceu!')
elif computador == 'PEDRA' and jogador == 'TESOURA' or computador == 'PAPEL' and jogador == 'PEDRA' or computador == 'TESOURA' and jogador == 'PAPEL':
    print(f'{computador} vence {jogador}. Você perdeu!')
elif jogador == computador:
    print(f'{jogador} com {computador} da empate.')
else:
    print('Opção inválida.')