# # Crie um programa que vai ler vários números e colocar em uma lista.  Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.  Ao final, mostre o conteúdo das três listas geradas

lista = []
pares = []
impares = []


while True:
    try:
        lista.append(float(input('Digite um número (Insira uma letra para parar): ')))
    except:
        break

lista.sort()

for i in lista:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)

print('-='*20)
print(f'Lista: {lista}')
print(f'Pares: {pares}')
print(f'Impares: {impares}')



