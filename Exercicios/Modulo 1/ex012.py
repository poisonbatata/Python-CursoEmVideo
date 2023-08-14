# Faça um algoritimo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
preço = float(input('Qual o preço do produto? '))
print('Com 5% de desconto ele custará R${}.'.format(preço-5/100*preço))