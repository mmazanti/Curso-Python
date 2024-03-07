nota1 = float(input('Digite o valor da primeira nota: '))
nota2 = float(input('Digite o valor da segunda nota: '))
media = (nota1+nota2)/2
if media < 5.0:
    print(f'REPROVADO! Sua média foi de {media:.2f}.')
elif media >= 5.0 and media <= 6.9:
    print(f'RECUPERAÇÃO! Sua média foi de {media:.2f}')
else:
    print(f'APROVADO! Sua média foi de {media:.2f}')