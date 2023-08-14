#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valor lido. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
continua = 's'
contagem = 0
soma = 0
media = 0
while continua == 's':
    num = int(input('Digite um número inteiro:'))
    contagem += 1
    soma += num
    media = soma/contagem
    continua = input('Deseja continuar? [s/N]').lower().strip()
    if contagem == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
print('A média foi:',media)
print('O maior valor foi:',maior)
print('O menor valor foi:',menor)
