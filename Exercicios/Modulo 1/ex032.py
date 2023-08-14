# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
n1 = int(input('Insira um ano: '))
if n1%4 == 0 and n1%100 != 0 or n1%400 == 0:
    print('É bissexto!')
else:
    print('Não é bissexto!')