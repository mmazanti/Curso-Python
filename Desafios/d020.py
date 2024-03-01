from random import shuffle
n1 = input('Nome do primeiro aluno: ')
n2 = input('Nome do segundo aluno: ')
n3 = input('Nome do terceiro aluno: ')
n4 = input('Nome do quarto aluno: ')
nomes = [n1, n2, n3, n4]
shuffle(nomes)
print('A ordem sorteada dos nomes foram: {}'.format(nomes))
