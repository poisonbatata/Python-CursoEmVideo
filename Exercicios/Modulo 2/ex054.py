# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
# O guanabara disse pra considerar a maioridade sendo 21, mas eu fiz sendo 18 msm
from datetime import datetime

menores = 0
maiores = 0
for i in range(0,7):
    ano = int(input('Digite em que ano você nasceu: '))
    now = datetime.now().year
    if now - 18 <= ano:
        maiores += 1
    elif now - 18 > ano:
        menores += 1
print('Maiores:',maiores)
print('Menores:',menores)
