# Desenvolva um programa que leia o comprimento de 3 retas e diga ao usuário se elas podem ou não formar um triângulo.
n1 = float(input('Digite o comprimento de uma reta: '))
n2 = float(input('Digite o comprimento de outra reta: '))
n3 = float(input('Digite o comprimento de mais outra reta: '))

if n1<n2+n3 and n2<n1+n3 and n3<n1+n2:
    print('Elas podem formar um triangulo!')
else:
    print('Elas não formam um triangulo!')

"""Meu jeito:
n1 = float(input('Digite o comprimento de uma reta: '))
n2 = float(input('Digite o comprimento de outra reta: '))
n3 = float(input('Digite o comprimento de mais outra reta: '))
e = 0
if n1 > n2 > n3:
    e = 1
elif n1 > n3 > n2:
    e = 2
elif n2 > n1 > n3:
    e = 3
elif n2 > n3 > n1:
    e = 4
elif n3 > n2 > n1:
    e = 5
elif n3 > n1 > n2:
    e = 6

if e == 1:
    if n1<n2+n3:
        print('Elas podem formar um triangulo! ')
    else:
        print('Elas não formam um triangulo!')
elif e == 2:
    if n1<n2+n3:
        print('Elas podem formar um triangulo! ')
    else:
        print('Elas não formam um triangulo!')
elif e == 3:
    if n2<n1+n3:
        print('Elas podem formar um triangulo! ')
    else:
        print('Elas não formam um triangulo!')
elif e == 4:
    if n2<n1+n3:
        print('Elas podem formar um triangulo! ')
    else:
        print('Elas não formam um triangulo!')
elif e == 5:
    if n3<n1+n2:
        print('Elas podem formar um triangulo! ')
    else:
        print('Elas não formam um triangulo!')
elif e == 6:
    if n3<n1+n2:
        print('Elas podem formar um triangulo! ')
    else:
        print('Elas não formam um triangulo!')
else:
    print('Elas não formam um triangulo!')
"""