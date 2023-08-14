# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.  Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla

from random import randrange

tupla = (randrange(0,10),randrange(0,10),randrange(0,10),randrange(0,10),randrange(0,10))
print(tupla)

''' Minha solução pra pegar o menor e maior valor: 
maior = tupla[0]
menor = tupla[0]

for i in tupla:
    if i > maior:
        maior = i
    if i < menor:
        menor = i

print(f'O maior número é o {maior}')
print(f'O menor número é o {menor}')
'''

# Solução do Guanabara: 

print(f'O maior número é o {max(tupla)}')
print(f'O menor número é o {min(tupla)}')
