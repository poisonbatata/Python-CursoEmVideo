'''

Variáveis Compostas (Listas) Parte 2

12/11/2021

Exercicios: 84 a 89
'''
# ESSA AULA ELE FALA SOBRE MATRIZ, só que sem falar "matriz"

"""

pessoas = list()
dados = ['Pedro', 25]
pessoas.append(dados[:])
dados = ['Maria', 19]
pessoas.append(dados[:])
dados = ['João', 32]
pessoas.append(dados[:])
print(pessoas)

print(pessoas[0][0]) # Pedro
print(pessoas[1][1]) # 19
print(pessoas[2][0]) # Joao
print(pessoas[1]) # ['Maria', 19]

"""


teste = list()
teste.append("Gustavo")
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)


galera = [['Joao', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera[0][0]) # Joao
print(galera[2][1]) # 13
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')


galera = list()
dado = list()
totmai = totmen = 0
for c in range(0, 3):
    dado.append(str(input("Nome: ")))
    dado.append(str(input("Idade: ")))
    galera.append(dado[:])
    dado.clear()
#print(galera)
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores de idade.')






