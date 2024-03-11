numero = int(input('Digite um número: '))
base_conversão = int(input('''\nEscolha a base de conversão:
[1] binário
[2] octal
[3] Hexadecimal
==> '''))
if base_conversão == 1:
    print(f'O número {numero} em binário é: {bin(numero)[2:]}')
elif base_conversão == 2:
    print(f'O número {numero} em octal é: {oct(numero)[2:]}')
elif base_conversão == 3:
    print(f'O número {numero} em hexadecimal é: {hex(numero)[2:]}')
else:
    print('Opção inválida.')