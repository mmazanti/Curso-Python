preço = float(input('Qual o valor do produto? R$ '))
condição_pagamento = int(input('''Escolha uma opção de pagamento:
[1] À vista dinheiro/cheque: 10% de desconto
[2] À vista no cartão: 5% de desconto.
[3] Parcelado até 2x sem juros no cartão.
[4] Parcelado 3x ou mais no cartão: 20% de juros.
==> '''))
if condição_pagamento == 1:
    preço = preço-(preço*0.1)
    print(f'À vista dinheiro/cheque: 10% de desconto. \nValor a ser pago: R$ {preço:,.2f}')
elif condição_pagamento == 2:
    preço = preço-(preço*0.05)
    print(f'À vista no cartão: 5% de desconto. \nValor a ser pago: R$ {preço:,.2f}')
elif condição_pagamento == 3:
    parcelado = preço/2
    print(f'Parcelado até 2x sem juros. \nValor a ser pago: R$ {preço:,.2f} em 2x de {parcelado:,.2f}')
elif condição_pagamento == 4:
    preço = preço+(preço*0.2)
    parcelado = int(input('Quantas vezes quer parcelar? '))
    valor_parcela = preço/parcelado
    print(f'Parcelado em {parcelado}x de R$ {valor_parcela:,.2f}. Valor total = R$ {preço:,.2f}')
else:
    print('Opção inválida.')
