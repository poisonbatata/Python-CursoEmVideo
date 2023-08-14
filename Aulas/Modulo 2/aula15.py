'''

Interrompendo repetições while


'''


cont = 1
while cont <= 10:
    print(cont,' -> ', end='')
    cont += 1
print('Acabou')


# Gambiarra : 
n = s =0
while n != 999:
    n = int(input('Digite um número: '))
    s += n
s -= 999
print('A soma vale {}'.format(s))

# Forma ideal:
n = s =0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
#print('A soma vale {}'.format(s))
print(f'A soma vale {s}')


nome = 'José'
idade = 33
salario = 987.35
print(f'O {nome} tem {idade} anos.') # PYTHON 3.6+
print('O {} tem {} anos.'.format(nome,idade)) #PYTHON 3
print('O %s tem %d anos.' % (nome, idade)) #PYTHON 2

print(f'O {nome} tem {idade} anos e ganha R${salario:.2f}.')





