# Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostr a matriz na tela, com a formatação correta.

matriz = [
    [],
    [],
    []
]

for i in range(1,10):
    num = int(input(f"Digite o {i}º número inteiro: "))
    if i in range(1,4):
        matriz[0].append(num)
    elif i in range(4,7):
        matriz[1].append(num)
    elif i in range(7,10):
        matriz[2].append(num)

print(f"""
[ {matriz[0][0]} ] [ {matriz[0][1]} ] [ {matriz[0][2]} ]
[ {matriz[1][0]} ] [ {matriz[1][1]} ] [ {matriz[1][2]} ]
[ {matriz[2][0]} ] [ {matriz[2][1]} ] [ {matriz[2][2]} ]
""")

