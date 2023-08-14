# Faça um programa que ajude a um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint
megasena = []

jogos = int(input("Quantos jogos serão? "))

for i in range(jogos):
    megasena.append(list()) # Criar jogos (listas) dentro da lista megasena
    for j in range(6):
        numero = randint(1,60)
        while True:
            if numero not in megasena[i]:
                megasena[i].append(numero)
                break
            elif numero in megasena[i]:
                numero = randint(1,60)
    print(f"Jogo {i+1}: {megasena[i]}")

