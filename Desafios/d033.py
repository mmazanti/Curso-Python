numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite outro número: '))
numero3 = int(input('Digite mais um número: '))
menor = numero1
if numero2<numero1 and numero2<numero3:
    menor = numero2
elif numero3<numero1 and numero3<numero2:
    menor = numero3
print('O menor valor digitado foi {}'.format(menor))
maior = numero1
if numero2>numero1 and numero2>numero3:
    maior = numero2
elif numero3>numero1 and numero3>numero2:
    maior = numero3
print('O maior valor digitado foi {}'.format(maior))