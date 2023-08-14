"""
Cores no Terminal


ANSI
escape sequence
\033[m

\033[ style text back  m
\033[0;33;44m
 

Style: 
    0  None
    1  Blod
    4  underline
    7  Negative

Text:
    30 Branco
    31 Vermelho
    32 Verde
    33 Amarelo
    34 Azul
    35 Magenta
    36 Ciano
    37 Cinza

Back:
    40 Branco
    41 Vermelho
    42 Verde
    43 Amarelo
    44 Azul
    45 Magenta
    46 Ciano
    47 Cinza
"""

print('\033[1;30;45mOlá, mundo!\033[m')
print('\033[7;30;47mOlá, mundo!\033[m')

a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m'.format(a,b))

nome = 'Guanabara'
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format('\033[4;34;47m',nome,'\033[m'))

nome = 'Guanabara'
cores = {'limpa':'\033[m','azul':'\033[34m','amarelo':'\033[33m','pretoebranco':'\033[7:30m'}
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format(cores['azul'],nome,cores['limpa']))