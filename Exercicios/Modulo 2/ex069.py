# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:  A) Quantas pessoas tem mais de 18 anos   B) Quantos homens foram cadastrados   C) Quantas mulheres com menos de 20 anos

print('-'*30)
print('{:^30}'.format('Cadastre uma pessoa'))
print('-'*30, end='\n\n')

continuar = 's'
sexo = 'a'
homem = 0
mulherMenos20 = 0
maior = 0

while continuar in 'Ss':
    idade = int(input('Idade: '))

    while sexo not in 'MmFf' : 
        sexo = input('Sexo: [M/F] ')

    if idade > 18:
        maior += 1
    if sexo in 'Mm':
        homem += 1
    if sexo in 'Ff' and idade < 20:
        mulherMenos20 += 1
    
    continuar = input('Deseja continuar? [S/n] ')
    while continuar not in 'SsNn':
        continuar = input('Deseja continuar? [S/n] ')

    print('~'*10)

print(f'Maiores de idade: {maior}')
print(f'Homens cadastrados: {homem}')
print(f'Mulheres com menos de 20 anos: {mulherMenos20}')
