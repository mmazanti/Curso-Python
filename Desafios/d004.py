print('Descubra qual o tipo primitivo')
obj = input('Digite algo: ')
print('É uma letra do alfabeto?', obj.isalpha())
print('É um número?', obj.isnumeric())
print('É um algarismo alphanumério?',obj.isalnum())
print('É um ASCII?',obj.isascii())
print('É um dígito de 0 a 9?',obj.isdigit())
print('É um número decimal?',obj.isdecimal())
print('É um identificador válido de variável?',obj.isidentifier())
print('Todos os caracteres são minúsculos?',obj.islower())
print('Todos os caracteres são imprimíveis para um dispositivo de saída?',obj.isprintable())
print('Todos os caracteres são espaços em branco?',obj.isspace())
print('É um título? Ou seja, o primeiro caracter é maiúsculo e os demais que o seguem são minúsculos?',obj.istitle())
print('Todos os caracteres são maiúsculos?',obj.isupper())