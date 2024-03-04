cidade = input('Digite o nome da cidade: ')
cidade_maiuscula = cidade.upper()
if cidade_maiuscula.startswith("SANTO"):
    print('O nome da cidade começa com Santo')
else:
    print('O nome da cidade não começa com Santo')