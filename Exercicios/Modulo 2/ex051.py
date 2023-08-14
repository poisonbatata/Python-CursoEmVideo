# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão
p1 = int(input('Digite o primeiro termo de uma PA: '))
r = int(input('Digite a razão da PA: '))

for i in range(0,10):
    print(p1 + r * i)