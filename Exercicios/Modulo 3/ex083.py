# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

texto = input('Expressão com parênteses: ')
verificador =  0
verdadeiro = True

for c, v in enumerate(texto):
    if v == "(":
        verificador += 1
    elif v == ")":
        verificador -= 1
        if verificador < 0:
            verdadeiro = False
            break

if(verdadeiro):
    if verificador != 0:
        print("Expressão inválida!")
    else:
        print("A expressão é válida!")
else:
    print("Expressão inválida!")

