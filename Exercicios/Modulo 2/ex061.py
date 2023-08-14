#Refaca o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

p1 = int(input('Digite o primeiro termo de uma PA: '))
r = int(input('Digite a razão da PA: '))
i = 0

while i < 10:
    print(p1 + r * i)
    i += 1
