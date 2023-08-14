# Faça um programa que leia o comprimento do cateto oposto e do cateto adijacente de um triangulo ret^rnauglo, calcule e mostre o compromento da hipotenusa.
from math import sqrt
co = float(input('Quanto vale o cateto oposto? '))
ca = float(input('Quanto vale o cateto adjacente? '))
hip = sqrt(pow(co,2)+pow(ca,2))
print('A hipotenusa vale',hip)
