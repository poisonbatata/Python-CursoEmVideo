# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.
# Fiz do meu jeito cm coisa q ele n ensinou ainda msm pq s
numero = int(input("Digite um número: "))
multiplicador = range(1,11)
for contagem in multiplicador:
    resultado = numero*contagem
    print('{} * {} = {}'.format(numero,contagem,resultado))