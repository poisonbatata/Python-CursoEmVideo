# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta se inserção (sem usar o sort()).  No final, mostre a lista ordenada na tela.

'''
# N vou continuar pq vai demorar, mas eu faria assim: (Uma verificação por cada numero inserido e ia ficar um código enorme td cagado)
# Dai pra adicionar um 3 entre num [2,5] eu verificaria a posição do último número maior q o 3 inserido e iria adicioná-lo ali
lista = []

num = lista.append(float(input(f'Digite um número: ')))
print(f'O {num} foi adicionado no final da lista')
anterior = num

num = float(input(f'Digite um número: '))
if num < anterior:
    lista.insert(0, num)
    print(f'O {num} foi adicionado na posição 0')

if num > anterior or num == anterior:
    print(f'O {num} foi adicionado no final da lista')
    lista.append(num)
'''


# Código do guanabara:
lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista')
                break
            pos += 1
print('-='*30)
print(f'Os valores digitados em ordem foram {lista}')

