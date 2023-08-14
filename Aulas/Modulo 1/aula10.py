nome = input('Qual é o seu nome? ')
if nome == 'Gustavo':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')
print('Bom dia, {}!'.format(nome))



n1 = float(input('Digite primeira a nota: '))
n2 = float(input('Digite segunda a nota: '))
m = (n1+n2)/2
print('A sua média foi {:.1f}'.format(m))
if m >= 6:
    print('Sua média foi boa! PARABENS!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')
print('PARABENS' if m >=6 else 'ESTUDE MAIS!')