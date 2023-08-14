# Faça um programa que leia o peso de 5 pessoas. No final, mostre qual foi o maior e o menor peso lidos.
# Usei o código do guanabara pq n consegui achar o peso menor
maior = 0
menor = 0
outro = 0
for i in range(0,5):
    peso = float(input('Digite seu peso: (em kg) '))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso é {}kg, e o menor é {}kg'.format(maior,menor))

"""
for i in range(0,5):
    peso = float(input('Digite seu peso: (em kg) '))
    if peso > maior:
        maior = peso

    elif peso < maior:
        outro = peso
        
    elif peso < outro:
        menor = peso 
"""