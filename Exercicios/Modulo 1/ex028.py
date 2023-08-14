# Escreva um programa que faça um computador 'pensar' em um numero inteiro entre 0 e 5 e peça para o usuario tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o uusuário venceu ou perdeu.
from random import randint
num = int(input('Tente adivinhar o meu número inteiro! (De 0 e 5): '))
ram = randint(0,5)
if num == ram:
    print('Você GANHOU! O número foi:',ram)
else:
    print('Você perdeu! O número era:',ram,'e você digitou',num)
