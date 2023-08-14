'''

Variáveis Compostas (Tuplas)

14/07/2021
'''

# As tuplas são imutáveis


lanche = 'Hambúrguer'
lanche = 'Suco'
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[1])
print(lanche[0:3])
print(lanche[:2])
print(lanche[:-3])

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')

for comida in lanche:
    print(f'Eu vou comer {comida}')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

print('Comi pra caramba!')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')




lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
print(sorted(lanche))
print(lanche)



a = (2,5,4)
b = (5,8,1,2,)
c = a + b
print(c)

c = b + a
print(c)

print(len(c))
print(c.count(5))

print(c.index(8)) # Ver a posição do numero 8 na tupla



pessoa = ('Gustavo', 39, 'M', 99.88)
del(pessoa)  # Aqui tu apaga a tupla da memória (N da pra apagar só 1 elemento da tupla, mas da pra apagar ela inteira)
print(pessoa)


