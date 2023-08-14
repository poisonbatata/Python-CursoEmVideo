# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

# Quero fazer uma função aqui pq sim
def jogo():
    global userPI
    global user
    global pc
    userPI = int(input('''
    [ 1 ] Par
    [ 2 ] Ímpar
    '''))
    user = int(input('Digite um número: '))
    pc = randint(0,11)




win = 0
while True:
    jogo()
    if userPI == 1 and (user+pc)%2 == 0:
        print('Usuário venceu!')
        win +=1

    elif userPI == 2 and (user+pc)%2 != 0:
        print('Usuário venceu!')
        win +=1

    else:
        print(f'Você perdeu com {win} pontos!')
        break


