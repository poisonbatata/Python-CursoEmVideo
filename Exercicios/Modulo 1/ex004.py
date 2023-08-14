# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ele
algo = input("Digite algo: ")
print('Só tem espaços? ',algo.isspace())
print('É um número? ',algo.isnumeric())
print('É alfabético? ',algo.isalpha())
print('É alfanumérico? ',algo.isalnum())
print('Está em maiúsculas? ',algo.isupper())
print('Está em minúsculas? ',algo.islower())
print('Está capitalizada? ',algo.istitle())
#print('',algo.is)
#print('',algo.is)

""" Fiz assim mas gostei mais da forma q o guanabara fez: 
if algo.isalpha() == True:
    print("Você digitou algum caractere")
if algo.isascii() == True:
    print("Você digitou algo da tabela ascii")
if algo.isdecimal() == True:
    print('Você digitou algo decimal')
if algo.isdigit() == True:
    print('Você digitou algum digito')
if algo.islower() == True:
    print('Você digitou algo em minúsculo')
if algo.isupper() == True:
    print('Você digitou algo em maiúsculo')
if algo.isidentifier() == True:
    print('Você digitou algo identificável')
if algo.isnumeric() == True:
    print('Você digitou algum numero')
if algo.isprintable() == True:
    print('Você digitou algo exibível')
if algo.isspace() == True:
    print("Você digitou um espaço")
if algo.istitle() == True:
    print('Você digitou um título')
if algo.isalnum() == True:
    print('Você digitou algo alphanumérico')
else:
    print('Vpcê não digitou nada!')
"""
#print("Fim :D")