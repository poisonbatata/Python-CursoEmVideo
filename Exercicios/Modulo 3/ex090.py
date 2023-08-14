# Faça um programa qaue leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela

aluno = {}

aluno['nome'] = input("Nome: ")
aluno['media'] = float(input("Média: "))

if aluno["media"] >= 7:
    aluno['situacao'] = 'Aprovado'
else:
    aluno['situacao'] = 'Reprovado'

for k,v in aluno.items():
    print(f"{k} é igual a {v}")


