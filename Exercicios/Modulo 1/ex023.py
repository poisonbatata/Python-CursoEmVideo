# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos sepadados. Ex: Digite um número 1834   unidade:4 dezena:3 centena:8 milhar:1
#forma do guanabara:
num=int(input('Informe um número de 0 a 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))


""" Minha forma de fazer : 
num = input('Digite um número de 0 a 9999: ')
if len(num) > 4:
    print('É só até 9999 seu batata')
if len(num) == 4:
    print('Milhar:  ',num[len(num)-4])
    print('Centena: ',num[len(num)-3])
    print('Dezena:  ',num[len(num)-2])
    print('Unidade: ',num[len(num)-1])
if len(num) == 3:
    print('Centena: ',num[len(num)-3])
    print('Dezena:  ',num[len(num)-2])
    print('Unidade: ',num[len(num)-1])
if len(num) == 2:
    print('Dezena:  ',num[len(num)-2])
    print('Unidade: ',num[len(num)-1])
if len(num) == 1:
    print('Unidade: ',num[len(num)-1])
if len(num) == 0:
    print('Tem que colocar algum número!')
"""