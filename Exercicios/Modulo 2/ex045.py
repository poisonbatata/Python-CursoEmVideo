# Crie um programa que faça o computador jogar Jokenpô com você
'''
pedra -> 1
papel -> 2
tesoura -> 3
'''
from random import randrange
player = int(input('Escolha:\n1)Pedra\n2)Papel\n3)Tesoura\n'))
computer = randrange(1,4)
#print(computer)
if player == computer:
    print('Empate!')
elif player == 1 and computer == 2: #Pedra e papel  PC WIN
    print('Você perdeu!')
elif player == 2 and computer == 1: #Papel e pedra PLAYER WIN
    print('Você ganhou!')
elif player == 1 and computer == 3: #Pedra e tessoura PLAYER WIN
    print('Você ganhou!')
elif player == 3 and computer == 1: #Tessoura e pedra PC WIN
    print('Você perdeu!')
elif player == 2 and computer == 3: #Papel e tesoura PC WIN
    print('Você perdeu!')
elif player == 3 and computer == 2: #Tessoura e papel PLAYER WIN
    print('Você ganhou!')