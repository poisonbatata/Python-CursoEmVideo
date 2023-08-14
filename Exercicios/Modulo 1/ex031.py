# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de atpe 200Km e R$0,45 para viagens mais longas.
n = float(input('Qual é a distãncia da viagem? '))
if n <= 200:
    print('O preço da viagem será R${:.2f}'.format(n*0.5))
else:
    print('O preço da viagem será R${:.2f}'.format(n*0.45))