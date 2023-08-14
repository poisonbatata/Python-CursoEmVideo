# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângilo será formado: -Equilátero:todos os lados iguais   -Isósceles:dois lados iguais   -Escaleno:todos os lados diferentes

n1 = float(input('Digite o comprimento de uma reta: '))
n2 = float(input('Digite o comprimento de outra reta: '))
n3 = float(input('Digite o comprimento de mais outra reta: '))

if n1<n2+n3 and n2<n1+n3 and n3<n1+n2:
    print('Elas podem formar um triangulo!')
    if n1 == n2 == n3: 
        print('Triângulo Equilátero')
    elif n1 == n2 or n1 == n3 or n2 == n3:#Isósceles
        print('Triângulo Isósceles')
    else:
        print('Triângulo Escaleno')
else:
    print('Elas não formam um triangulo!')
