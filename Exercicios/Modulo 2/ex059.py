# Crie um programa que leia 2 valores e mostre o menu na tela: [1]somar  [2]multiplicar  [3]maior  [4]novos numeros  [5]sair do programa
menu = 0
n1 = float(input("Digite 1 numero: "))
n2 = float(input("Digite o 2 numero: "))
while menu != 5:
    menu = int(input('''
    [1]somar
    [2]multiplicar
    [3]maior
    [4]novos numeros
    [5]sair do programa
    '''))
    if menu == 1:
        print('A soma e: ',n1+n2)
    elif menu == 2:
        print("A multiplicacao e: ",n1*n2)
    elif menu == 3:
        if n1 > n2:
            print('O primeiro valor eh o maior')
        else:
            print('O segundo valor eh o maior')
    elif menu == 4:
        n1 = float(input("Digite 1 numero: "))
        n2 = float(input("Digite o 2 numero: "))
print("Fim do programa")
