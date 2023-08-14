# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

n = 0

while True:
    n = int(input('Digite um número (negativo para parar): '))
    if n < 0:
        print('-='*20)
        print('Programa encerrado!')
        break
    for i in range(1,11):
        print(f'{n} * {i} = {n*i}')