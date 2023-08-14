# Faça um programa que leia um número inteiro e diga se ele é ou não primo
n1 = int(input('Digite um número inteiro: '))

s = 0
# Verificando se é primo um número maior que 9
if n1 > 9:
    for i in range(1, 10):
        if n1 % i == 0:
            s += 1
    if s != 1:
        print('Não é um número primo!')
    else:
        print('É primo!')
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# Verificando se é primo um número menor que 9
elif n1 < 10:
    for i in range(1, 10):
        if n1 % i == 0:
            s += 1
    if s != 2:
        print('Não é um número primo!')
    else:
        print('É primo!')
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

if n1 == 1:
    print('É primo!')