# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: -A média de idade do grupo  -Qual é o nome do homem mais velho  -Quantas mulheres têm menos de 20 anos.
# Peguei o codigo do guanabara pq n fiz esse
somaIdade = 0
mediaIdade = 0
maioridadeHomem = 0
nomeVelho = ''
mulher20 = 0
for i in range(1,5):
    print('---- {}ª PESSOA ----'.format(i))
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip()
    somaIdade += idade
    if i == 1 and sexo in "Mm":
        maioridadeHomem = idade
        nomeVelho = nome
    if sexo in 'Mm' and idade > maioridadeHomem:
        maioridadeHomem = idade
        nomeVelho = nome
    if sexo in 'Ff' and idade < 20:
        mulher20 += 1

mediaIdade = somaIdade/4
print('A média da idade do grupo é de {} anos'.format(mediaIdade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridadeHomem, nomeVelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(mulher20))