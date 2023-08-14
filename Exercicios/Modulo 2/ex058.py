# Melhore o jogo do DESAFIO 028 onde o computador vai 'pensar' em um numero entre 0 e 10. So que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram cenessários para vencer.

from random import randint
num = int(input('Tente adivinhar o meu número inteiro! (De 0 a 10): '))
ram = randint(0,10)
print(ram)
a = 1
while num != ram:
    print('Errou! Tente novamente!')
    num = int(input('Digite novamente: (De 0 e 10): '))
    a += 1

print('\nVocê ganhou!')
print('Foram necessárias {} tentativas para vencer!'.format(a))
