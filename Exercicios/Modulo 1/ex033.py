# Faça um programa que leia 3 numeros e mostre qual é o maior e qual é o menor
n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
n3 = float(input('Digite mais outro número: '))

menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3

maior = n1
if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3
print('O maior valor é {} e o menor é {}'.format(maior,menor))


""" Meu jeito:
if n1 > n2 > n3:
    print(n1,'é o maior. O menor é',n3)
elif n2 > n1 > n3:
    print(n2,'é o maior. O menor é',n3)
elif n3 > n2 > n1:
    print(n3,'é o maior. O menor é',n1)
elif n2 > n3 > n1:
    print(n2,'é o maior. O menor é',n1)
elif n1 > n3 > n2:
    print(n1,'é o maior. O menor é',n2)
elif n3 > n1 > n2:
    print(n3,'é o maior. O menor é',n2)
else:
    print('Tem algum numero igual ae')
"""