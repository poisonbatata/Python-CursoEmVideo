# Escreva um programa que pergunte o salário de um funcioário e calcule o valor do seu aumento. Para salários superiores a R$1.250,00, calcule um aumento de 10%.  Para os inferiores ou iguais, o aumento é de 15%
n1 = float(input('Digite seu salário: '))
if n1 > 1250:
    print('Seu novo salário será: {}'.format(10/100*n1+n1))
else:
    print('Seu novo salário será: {}'.format(15/100*n1+n1))