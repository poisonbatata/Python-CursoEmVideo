# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ínpares em ordem crescente.

geral = [[],[]]

for i in range(1,8):
    num = int(input(f"Digite o {i}º número inteiro: "))
    if num%2==0 or num==0:
        geral[0].append(num)
    elif num%2!=0:
        geral[1].append(num)

geral[0].sort()
geral[1].sort()

print(f'Pares: {geral[0]}')
print(f'Ímpares: {geral[1]}')
