# Faça um programa que leia a largura e a altura de uma parece em metros, calcule sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²
h = float(input('Qual a altura da parede? '))
l = float(input('Qual a largura da parede? '))
area = h*l
print('Você precisará de {} litros de tinta para pintar essa parede de {}m².'.format(area/2,area))