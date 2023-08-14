# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.   Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou entao o empréstimo será negado.

casa = float(input('Qual o preço da casa? '))
sal = float(input('Qual seu salário? '))
ano = float(input('Em quantos anos você irá pagar? '))

prest = casa/(ano*12)
maximo = 30/100*sal

if prest > maximo:
    print('Nada de empréstimo!')
else:
    print('Empréstimo aceito!')
