# faca um programa que leia o sexo de uma pessoa, mas so aceite os valores 'M' ou 'F'. Caso esteja errado, peca a digitacao novamente ate ter um valor correto
sexo = 'a'
while sexo != 'M' and 'F':
    sexo = input('Qual e o seu sexo? [M/F]').upper().strip()
    if sexo != 'M' and 'F':
        print('Digite o valor novamente. ')
