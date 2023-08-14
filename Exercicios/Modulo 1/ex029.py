# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/H, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
vel = float(input('Digite a velocidade do carro em Km/h : '))
if vel > 80:
    print('Você será multado em R${:.2f}'.format((vel-80)*7))
else:
    print('Ta safe!')