# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalho dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import shuffle
n1 = input('Digite o 1º nome: ')
n2 = input('Digite o 2º nome: ')
n3 = input('Digite o 3º nome: ')
n4 = input('Digite o 4º nome: ')
nomes = [n1,n2,n3,n4]
shuffle(nomes)
print('A ordem de apresentação será',nomes)