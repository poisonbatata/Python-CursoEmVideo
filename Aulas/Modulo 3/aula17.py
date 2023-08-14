'''

Variáveis Compostas (Listas) Parte 1

25/07/2021

Exercicios: 78 ao 89
'''


""" Aqui eu escrevi as coisas q ele foi explicando, a parte prática ta sem estar comentada mais em baixo
# Lista
lanche = ['bugão','suco','pizza','sorvete', 'pizza']

# Adicionar valores na Lista
lanche.append('cookie') # Adiciona o 'coockie' no final da lista
lanche.insert(0,'batata') # Adiciona o 'batata' na posição desejada

# Remover valores da Lista
del lanche[3] # Apaga o elemento na posição 3 da lista
lanche.pop(3) # Normalmente o .pop apaga o ultimo elemento, mas da pra selecionar qual a posição do que deverá ser apagado
lanche.remove('pizza') # Apaga a primeira ocorrência do elemento 'pizza'

# Se o valor passado no .remove não estiver na lista, vai dar erro! Dai tem q fazer uma verificação antes.
if 'pizza' in lanche:
    lanche.remove('pizza')



# Criar Listas a partir do range()
valores = list(range(4,11)) # Cria uma lista que vai do 4 até o 10
valores = list(range(4,11,3)) # Cria uma lista que vai do 4 até o 10 pulando de 3 em 3

valores = [8,2,5,4,9,3,0]
valores.sort() # O .sort organiza todos os elementos e os coloca em ordem crescente
valores.sort(reverse=True) # Dai aqui será em ordem decrescente

len(valores) # Descobre o tamanho de uma lista
"""


num = [2,5,9,1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2,0)
num.pop()
num.pop(2)
print(num)
print(f'Essa lista tem {len(num)} elementos')

num.insert(2,2)
num.remove(2)
print(num)


if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4')
print(num)


# Da pra criar uma lista vazia desses 2 jeitos: 
valores = list()
valores = []

valores.append(5)
valores.append(9)
valores.append(4)

for c,v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}')
print('Cheguei ao final da lista.')


for cont in range(0,5):
    valores.append(int(input('Digite um valor: ')))
for c,v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}')
print('Cheguei ao final da lista.')



# -=-=-=- IMPORTANTE -=-=-=-
# Se vc fizer b = a  o python faz uma ligação entre as 2 listas, dai se mudar uma, muda a outra também.
# Para que isso não ocorra, tem q fazer assim: b = a[:]  # Pq dai aqui o b vai receber uma cópia de tds os elementos de a
a = [2,3,4,7]
b = a
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')


c = [2,3,4,7]
d = c[:]
d[2] = 8
print(f'Lista C: {c}')
print(f'Lista D: {d}')

