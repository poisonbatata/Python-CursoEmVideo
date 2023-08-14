# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.  No final, mostre uma listagem de preços, organizando os dados em forma tabular.
listagem = ('Pão', 1.00, 'Leite', 3.50, 'Frango', 10.90)

print('-'*50)
print('{:^50}'.format('LISTAGEM DE PREÇOS'))
print('-'*50)

for i in range(0, len(listagem)):
    if i % 2 == 0:
        print(f'{listagem[i]:.<30}', end='')
    else:
        print(f'R${listagem[i]:>7.2f}')

print('-'*50)

