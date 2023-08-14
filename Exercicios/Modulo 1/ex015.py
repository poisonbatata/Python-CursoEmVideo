# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 reais por dia e R$0,15 por KM rodado.
dias = int(input('Quantos dias alugado? '))
km = float(input('Quantos km rodados? '))
print('Você terá que pagar R${:.2f}.'.format(dias*60+km*0.15))