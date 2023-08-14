# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

continuar = 's'
lista = []

while continuar in 'SsSIMsimSim':
    num = float(input('Digite um número: '))
    if num in lista:
        print(f'O número {num} já foi escolhido!')
    else:
        lista.append(num)
    continuar = input('Deseja continuar? [S/n]')

lista.sort()
print(lista)
print('Fim')

