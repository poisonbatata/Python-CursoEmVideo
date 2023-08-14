# Escreva um programa que leia um valor em metros e exiba convertido em centímetros e milímetros
n1 = float(input('Digite um valor em metros: '))
print('Este valor equivale a {} centímetros e a {} milímetros'.format(n1/100,n1/1000))