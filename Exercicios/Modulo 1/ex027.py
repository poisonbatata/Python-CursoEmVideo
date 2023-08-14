# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente. Ex: Ana Maria de Souza   primeiro = Ana  último = Souza
nome = input('Digite um nome: ')
tamanho = nome.split()
print('primeiro = ',tamanho[0])
#print('ultimo = ',tamanho[0::-1])
print('ultimo = ',tamanho[len(tamanho)-1])