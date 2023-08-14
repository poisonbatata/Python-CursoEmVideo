# Crie um programa que leia uma grase e diga se ela é um palíndromo, desconsiderando os espaços.
frase = input('Digite uma frase: ').replace(' ', '').lower()  # Daria pra usar o .strip(), porém ele só removeria os espaços do começo e do final

if frase == frase[::-1]:
    print('É um palíndromo')
else:
    print('Não é palíndromo.')

