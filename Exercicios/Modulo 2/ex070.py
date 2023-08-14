# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:  A) Qual é o total gasto na compra   B) Quantos produtos custam mais de R$1000,00   C) Qual é o nome do produto mais barato

print('-'*30)
print('{:^30}'.format('LOJA FEIRINHA ORGANICA'))
print('-'*30, end='\n\n')

continuar = 's'
total = 0
caros = 0
barato = ''
precoMenor = 0


produto = input('Produto: ')
preco = float(input('Preço: '))
precoMenor = preco
barato = produto
total += preco
if preco > 1000:
    caros += 1  
continuar = input('Deseja continuar? [S/n] ')
print('~'*10) 

while continuar in 'Ss':
    produto = input('Produto: ')
    preco = float(input('Preço: '))
    
    total += preco
    if preco > 1000:
        caros += 1
    if preco < precoMenor:
        precoMenor = preco
        barato = produto
    
    continuar = input('Deseja continuar? [S/n] ')
    print('~'*10) 

print('+'*15)
print('{:^15}'.format('Notas finais'))
print('+'*15)

print(f'Preço total: R${total:.2f}')
print(f'{caros} produtos custam mais de R$1000,00')
print(f'O produto mais barato foi o {barato}, custando R${precoMenor:.2f}', end='\n\n')
