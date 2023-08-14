# Faca um programa que leia um numero qlqr e mostre seu fatorial

n1 = float(input("Digite um numero qualquer: "))
n2 = n1
soma = 1
a = n2
while n2 != 0:
    soma = a * soma
    a = n2 - 1
    n2 = a
if n1 != 0:
    print('O fatorial de {} eh {}'.format(n1, soma))
else:
    print('O fatorial de {} eh {}'.format(n1, 0))
