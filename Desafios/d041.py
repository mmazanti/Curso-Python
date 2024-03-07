from datetime import datetime
ano_nascimento = int(input('Em que ano você nasceu? '))
ano_atual = datetime.now().year
idade = ano_atual - ano_nascimento
if idade <= 9:
    print('Categoria MIRIM.')
elif idade >= 10 and idade <= 14:
    print('Categoria INFANTIL.')
elif idade >= 15 and idade <= 19:
    print('Categoria JUNIOR.')
elif idade == 20:
    print('Categoria SÊNIOR.')
else:
    print('Categoria MASTER.')