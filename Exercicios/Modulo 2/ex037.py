# Escreva um programa que leia um número inteiro qlqr e peça para o usuário escolher qual será a base de conversão:  - 1 para binário   -2 para octal   -3 para hexadecimal

num = int(input('Digite um número que será convertido: '))
base = int(input('Insita a base de conversão: \n1 para binário \n2 para octal \n3 para hexadecimal\n'))

if base == 1:
    print('O valor {} em binário é {}'.format(num,bin(num)))
elif base == 2:
    print('O valor {} em octal é {}'.format(num,oct(num)))
elif base == 3:
    print('O valor {} em hexadecimal é {}'.format(num,hex(num)))
else:
    print('Opção inválida!')