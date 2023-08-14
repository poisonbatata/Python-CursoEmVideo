# Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
# O 009 eu já tinha feito com for kkkkkk entao só copiei pra cá
numero = int(input("Digite um número: "))
multiplicador = range(1,11)
for contagem in multiplicador:
    resultado = numero*contagem
    print('{} * {} = {}'.format(numero,contagem,resultado))