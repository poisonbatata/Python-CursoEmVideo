# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar. Considere US$1,00 = R$3,27
n1 = float(input('Quanto reais há na carteira?'))
print('Você poderá comprar {:.2f} dolares.'.format(n1/3.27))