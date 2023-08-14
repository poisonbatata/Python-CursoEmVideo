# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
cidade = input('Digite o nome de uma cidade: ')
if cidade.upper().strip().find('SANTO') == 0:
    print('A cidade "{}" começa com a palavra SANTO.'.format(cidade))