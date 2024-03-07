reta1 = float(input('Digite o comprimento da primeira reta: '))
reta2 = float(input('Digite o comprimento da segunda reta: '))
reta3 = float(input('Digite o comprimento da terceira reta: '))
if reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta2 + reta3 > reta1:
    if reta1 == reta2 and reta1 == reta3:
        print('Com essas medidas, forma-se um triângulo equilátero, quando todos os lados são iguais.')
    elif reta1 == reta2 or reta1 == reta3 or reta2 == reta3:
        print('Com essas medidas, forma-se um triângulo isósceles, quando dois lados são iguais.')
    else:
        print('Com essas medidas, forma-se um triângulo escaleno, quando todos os lados são diferentes.')
else:
    print('Com as medidas de retas informadas, não é possível formar um triângulo.')