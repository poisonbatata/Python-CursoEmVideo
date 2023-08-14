# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

lista = []

while True:
    nome = input("Digite seu nome:(SAIR para parar) ")
    if nome == "SAIR":
        break
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1+nota2)/2
    lista.append([nome, [nota1, nota2], media])

print("="*26)
print(f"{'No.':<4}{'NOME':<10}{'MÉDIA':>8}")
print('-'*26)

for c,v in enumerate(lista):
    print(f"{c:<4}{v[0]:<10}{v[2]:>8.1f}")


while True:
    print('='*35)
    opcao = int(input("Mostar notas de qual aluno?(-1 para parar) "))
    if opcao != -1:
        break
    if opcao <= len(lista)-1:
        print(f'Notas de {lista[opcao][0]} são {lista[opcao][1]}')




