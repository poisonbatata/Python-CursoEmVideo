# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que pe a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
num = 0
c = 0
soma = 0
while num != 999:
    num = int(input('Digite um número inteiro [999 para parar]: '))
    c +=1
    soma +=num
print(c-1)
print(soma-999)