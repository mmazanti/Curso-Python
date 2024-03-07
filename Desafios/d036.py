print("="*40)
print("             EMPRÉSTIMO")
print("="*40)
valor_imovel = float(input('Qual é o valor do imóvel? R$ '))
salario = float(input('Qual o seu salário? R$ '))
anos = int(input('Em quantos anos você pretende pagar? '))
prestação = valor_imovel / (anos*12)
limite = salario*0.3
if prestação > limite:
    print('Infelizmente, não é possível financiar esse imóvel. Valor da prestação mensal é superior a 30% do seu salário.')
else:
    print(f'O valor do imóvel: R$ {valor_imovel:,.2f}. \nValor da prestação mensal: R$ {prestação:,.2f}'.replace(',', '.'))
