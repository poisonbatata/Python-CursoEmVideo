'''

Estrutura de repeticao while
Lacos de repeticao parte 2


'''


"""
for c in range(1, 10):
    print(c)
print("fim")
"""

c = 1
while c < 10:
    print(c)
    c += 1
print("Fim")

n = 1
while n != 0:
    n = int(input("Digite um inteiro: "))
print("fim")

r = 's'
while r == 's':
    n = int(input("Digite um inteiro: "))
    r =  input("Quer continuar? [s/N]").lower()
print("fim")

n = 1
par = impar = 0
while n != 0:
    n = int(input("digite um valor: "))
    if n % 2 == 0:
        par += 1
    else:
        impar += 1
print("Pares: {}   Impares: {}".format(par, impar))
