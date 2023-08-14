# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.   No final, mostre qual foi o maior e o menor valor digitado e nas suas respectivdas posições na lista.

lista = []
for i in range(0,5):
    lista.append(int(input(f'Digite o número inteiro na posição {i}: ')))

listaB = lista[:]
lista.sort()

maior = lista[len(lista)-1]
menor = lista[0]

print(f'Maior: {maior} na posição',end=' ')
for c,v in enumerate(listaB):
    if v == maior:
        print(f'{c}', end=' ')


print(f'\nMenor: {menor} na posição {c}', end=" ")
for c,v in enumerate(listaB):
    if v == menor:
        print(f'{c}', end=' ')

