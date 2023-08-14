# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final mostre: A)Quantas pessoas foram cadastradas.  B)Uma listagem com as pessoas mais pesadas.   C)Uma listagem com as pessoas mais leves.

continuar = 'S'
pessoas = []
pesos = []
maiorPeso = 0.0
posicaoMaiorPeso = []
menorPeso = 0.0
posicaoMenorPeso = []

while continuar in "SsSIMsimSimsIM":
    pessoa = input("Digite seu nome: ")
    pessoas.append(pessoa)
    peso = float(input("Qual seu peso? "))
    pesos.append(peso)
    continuar = input("Deseja continuar?[S/n] ")
    if len(pesos) == 1:
        menorPeso = pesos[0]


# A)
print(f'\nForam cadastradas {len(pessoas)} pessoas.')


# B)
# Descobrir o maior peso
for i in pesos:
    if i > maiorPeso:
        maiorPeso = i
# Pegar as posições dos maiores pesos na lista
for c,v in enumerate(pesos):
    if v == maiorPeso:
        posicaoMaiorPeso.append(c)
# Printar o maior peso e as pessoas de maior peso
print(f'Maior peso: {maiorPeso}kg. Peso de', end=" ")
for i in posicaoMaiorPeso:  print(f'"{pessoas[i]}"', end=" ")


# C)
# Descobrir o menor peso
for i in pesos:
    if i < menorPeso:
        menorPeso = i
# Pegar as posições dos menores pesos na lista
for c,v in enumerate(pesos):
    if v == menorPeso:
        posicaoMenorPeso.append(c)
# Printar o menor peso e as pessoas de menor peso
print(f'\nMenor peso: {menorPeso}kg. Peso de', end=" ")
for i in posicaoMenorPeso:  print(f'"{pessoas[i]}"', end=" ")
