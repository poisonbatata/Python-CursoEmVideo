# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre: A)Quantas vezes apareceu o valor 9   B)Em que posição foi digitado o primeiro valor 3   C) Quais foram os numeros pares


tupla = (int(input('Digite um numero: ')), int(input('Digite um numero: ')), int(input('Digite um numero: ')), int(input('Digite um numero: ')))

print(f'O 9 apareceu {tupla.count(9)} vezes')


# O guanabara n ensinou try except ainda, mas decidi usar aqui assim msm
try: 
    print(f'O 3 apareceu primeiro na posição {tupla.index(3)}')
except:
    print('O número 3 não foi digitado.')


print(f'Os números pares são: ', end='')
for i in tupla:
    if i % 2 == 0:
        print(f'{i}', end=' ')

