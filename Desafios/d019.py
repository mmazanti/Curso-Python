from random import choice
n1 = input('Nome do primeiro aluno: ')
n2 = input('Nome do segundo aluno: ')
n3 = input('Nome do terceiro aluno: ')
n4 = input('Nome do quarto aluno: ')
nomes = [n1, n2, n3, n4]
sorteado = choice(nomes)
print('O nome sorteado foi: {}'.format(sorteado))