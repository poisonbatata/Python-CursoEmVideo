# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import sin,cos,tan,radians
n1 = float(input('Digite o valor de um ângulo: '))
sen = sin(radians(n1))
cos = cos(radians(n1))

if tan(radians(n1)) > 1 :
    print('A tangente de ',n1,'º não existe!')
    print('O seno é {:.2f}, cosseno {:.2f}'.format(sen,cos))
else:
    tan = tan(radians(n1))
    print('O seno é {:.2f}, cosseno {:.2f} e tangente {:.2f}'.format(sen,cos,tan))
