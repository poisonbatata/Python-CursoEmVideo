# Crie um programa que vai ler vários números e colocar em uma lista.  Depois disso mostre:   A) Quantos numeros foram digitados.   B)A lista de valores, ordenada de forma decrescente.   C)Se o valor 5 foi digitado e está ou não na lista

continuar = 's'
contador = 0
lista = []

while continuar in "SsSIMsimSimsIM":
    lista.append(int(input('Digite um valor: ')))
    continuar = input('Deseja continuar? [S/n]')
    contador += 1

print(f'\nForam digitados {contador} números.')
lista.sort(reverse=True)
print(lista)

if 5 in lista:
    print(f'O valor 5 está na lista.')
else:
    print('Nada de 5 na lista')


