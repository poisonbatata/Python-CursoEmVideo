# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude a ele, lendo o nome deles e escrevendo o nome escolhido.
from random import choice
n1 = input('Digite o 1º nome: ')
n2 = input('Digite o 2º nome: ')
n3 = input('Digite o 3º nome: ')
n4 = input('Digite o 4º nome: ')
nomes = [n1,n2,n3,n4]
print('O aluno escolhido foi o {}.'.format(choice(nomes)))