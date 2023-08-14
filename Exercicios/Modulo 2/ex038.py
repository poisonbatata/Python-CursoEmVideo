# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem: -O 1º valor é maior   -O 2º valor é maior  -Não existe valor maior, os 2 são iguais

n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite um outro número inteiro: '))

if n1 > n2:
    print('O primeiro valor é maior que o segundo!')
elif n2>n1:
    print('O segundo valor é maior que o primeiro!')
else:
    print('Os dois valores são iguais!')