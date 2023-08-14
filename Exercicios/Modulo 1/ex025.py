# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
nome = input('Digite um nome: ').strip()
if nome.upper().find('SILVA') != -1:
    print('O nome "{}"Ca possui a palavra SILVA.'.format(nome))