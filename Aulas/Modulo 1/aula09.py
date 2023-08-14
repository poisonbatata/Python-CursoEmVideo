"""
Manipulando texto

frase = 'Curso em Vídeo Python'

- Fatiamento
frase[9]   --> Pega apenas o 10º caractere  (a contagem começa no 0)
frase[9:13] --> Vai do 10ºcaractere até o 13º
frase[9:21]
frase[9:21:2] --> Vai do 10º até o 20º pulando de 2 em 2
frase[:5] --> Começa do 1º até o 4º
frase[15:] --> vai do 16º até o final
frase[9::3] --> Começa no 10º e vai até o final pulando de 3 em 3


- Análise
len(frase)  --> Comprimento de frase
frase.count('o') --> Conta qnts vezes aparece o 'o'
frase.count('o',0,13) --> Conta qnts vezes aparece o 'o' do 0 ao 12
frase.find('deo')  --> Mostra em que momento começou o 'deo'
frase.find('Android') --> Como n existe 'Android' dentro de frase, ele retornará -1
'Curso' in frase --> True


- Transformação
frase.replace('Python','Android') --> Vai trocar o 'Python' por 'Android' em frase
frase.upper() --> Vai deixar tudo em maiúsculas
frase.lower() --> Vai deixar tudo em minúsculas
frase.capitalize() --> Vai deixar o primeiro caractere em maiúsculo e todo o resto em minúsculo
frase.title() --> Vai deixar todo o primeiro caractere de cada palavra em maiúsculo e o resto em minúsculo

frase = '    Aprendendo Python  '

frase.strip() --> vai remover esses espaços iniciais e finais desnecessários
frase.rstrip() --> Remove somente os ultimos espaços
frase.lstrip() --> Remove somente os primeiros espaços

frase = 'Curso em Vídeo Python'


- Divisão
frase.split() --> Vai dividir as palavras da string baseando-se nos espaços e gera uma lista


- Junção
'-'.join(frase) --> Vai juntar as palavras com '-' baseando-se nos espaços


"""

frase = 'Curso em Vídeo Python'
print(frase[::2])

print('Oi')

print(""" 
Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Sed sagittis vel erat in congue. Donec et est non turpis semper sagittis non vel lacus. Donec luctus id neque sed viverra. Nullam neque elit, pretium eu magna eget, bibendum aliquam erat. Phasellus vestibulum diam consectetur, molestie velit vitae, convallis nunc. Suspendisse consequat, urna at ultrices tempor, justo neque interdum justo, sed suscipit erat elit vitae augue. Donec placerat eu arcu a luctus. Proin mi eros, hendrerit eget ipsum nec, mollis dapibus metus. Nullam mattis nunc nec ornare accumsan.
""")

print(frase.count('o'))
print(frase.count('O'))
print(frase.upper().count('O'))
print(len(frase))

frase = '   Curso em Vídeo Python   '
print(len(frase))
print(len(frase.strip()))

frase = 'Curso em Vídeo Python'
print(frase.replace('Python','Android'))

frase = 'Curso em Vídeo Python'
frase.replace('Python','Android')
print(frase)

frase = 'Curso em Vídeo Python'
frase = frase.replace('Python','Android')
print(frase)

frase = 'Curso em Vídeo Python'
print('Curso' in frase)

frase = 'Curso em Vídeo Python'
print(frase.find('Vídeo'))

frase = 'Curso em Vídeo Python'
print(frase.split())
dividido = frase.split()
print(dividido[2][3])
