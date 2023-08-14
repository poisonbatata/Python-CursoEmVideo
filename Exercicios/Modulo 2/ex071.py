# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.   OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1

print('-'*30)
print('{:^30}'.format('BANCO CEV'))
print('-'*30, end='\n\n')

quantia = int(input('Valor a sacar: R$'))

c50 = quantia // 50
if quantia % 50 != 0:
    c20 = (quantia - c50*50) // 20
    valor = (quantia - c50*50 - c20*20)
    if valor % 20 != 0:
        c10 = valor // 10
        valor = (quantia - c50*50 - c20*20 - c10*10)
        if valor % 10 != 0:
            c1 = valor // 1

print('Notas de R$50:',c50)
print('Notas de R$20:',c20)
print('Notas de R$10:',c10)
print('Notas de R$1:',c1)

