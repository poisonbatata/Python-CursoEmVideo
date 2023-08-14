# Aprimore o desafio anterior, mostrando no final: A)A soma de todos os valores pares digitados.  B)A soma dos valores da terceira coluna.  C)O maior valor da segunda linha.

somaPares = 0
somaTerceiraColuna = 0

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
    
    if num%2==0:
        somaPares += num

print(f"""
[ {matriz[0][0]} ] [ {matriz[0][1]} ] [ {matriz[0][2]} ]
[ {matriz[1][0]} ] [ {matriz[1][1]} ] [ {matriz[1][2]} ]
[ {matriz[2][0]} ] [ {matriz[2][1]} ] [ {matriz[2][2]} ]
""")


# A)
print(f"Soma dos pares: {somaPares}")

# B)
print("Soma da 3º coluna: {}".format(matriz[0][2]+matriz[1][2]+matriz[2][2]))

# C)
maiorValorSegundaLinha = matriz[1][0]
if matriz[1][1] > maiorValorSegundaLinha:
    maiorValorSegundaLinha = matriz[1][1]
if matriz[1][2] > maiorValorSegundaLinha:
    maiorValorSegundaLinha = matriz[1][2]

print(f"Maior valor da 2º linha: {maiorValorSegundaLinha}")

