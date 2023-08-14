# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade: -Se ele ainda vai se alistar ao serviço militar. -Se é a hora de se alistar. -Se já passou do tempo do alistamento.   Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import datetime
ano = int(input('Em que ano você nasceu? '))
atual = datetime.now()
print(atual.year)
idade = atual.year - ano

if idade < 18:
    print('Você deverá se alistar daqui a {} anos.'.format(18-idade))
elif idade > 18:
    print('Você deveria ter se alistado a {} anos.'.format(idade-18))
else:
    print('Está na hora de você se alistar!')