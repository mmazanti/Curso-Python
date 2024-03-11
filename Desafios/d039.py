from datetime import datetime
ano_nascimento = int(input('Qual ano você nasceu? '))
ano_atual = datetime.now().year
idade = ano_atual - ano_nascimento
if idade < 18:
    print(f'Ainda não chegou a hora do seu alistamento. Seu alistamento será em {ano_nascimento+18}.')
elif idade == 18:
    print('Chegou o ano do seu alistamento.')
else:
    print(f'Você passou {ano_atual-(ano_nascimento+18)} anos do tempo do alistamento.')
