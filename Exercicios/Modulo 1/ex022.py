# Crie um programa que leia o nome completo de uma pessoa e mostre: - O nome com todas as letras maiúsculas   - O nome com todas minúsculas   - Quantas letras ao todo(sem considerar espaços)    - Quantas letras tem o primeiro nome
nome = input('Qual seu nome? ')
print(nome.upper())
print(nome.lower())
print('Seu nome ao todo tem',len(nome.strip().replace(' ','')),'letras.')
lista = nome.split()
print('Seu primeiro nome tem',len(lista[1].strip()) - 1,'letras.')