salario = float(input('Qual o seu salário? R$ '))
if salario > 1250.0:
    aumento = salario*0.1+salario
    print('Seu aumento foi de 10%. Seu novo salário é de R$ {:.2f}'.format(aumento))
else:
    aumento = salario*0.15+salario
    print('Seu aumento foi de 15%. Seu novo salário é de R$ {:.2f}'.format(aumento))