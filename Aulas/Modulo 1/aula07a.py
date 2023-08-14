"""
Operadores aritiméticos:
+ Adição
- Subtração
* Multiplicação
/ Divisão
** Potência
// Divisão inteira
% Resto da divisão


Para tirar a raiz quadrada de um número basta eleva-lo a 1/2: 
81**(1/2) == 9
25**(1/2) == 5
127**(1/3) == 5.026525...


Ordem de precedência:
1º ()
2º **
3º * / // %
4º + -
"""
nome = input('Qual é o seu nome? ')
print('Prazer em te conhecer {}!'.format(nome))
print('Prazer em te conhecer {:20}!'.format(nome))
print('Prazer em te conhecer {:<20}!'.format(nome))
print('Prazer em te conhecer {:>20}!'.format(nome))
print('Prazer em te conhecer {:^20}!'.format(nome))
print('Prazer em te conhecer {:=^20}!'.format(nome))

n1 = int(input('Um valor numérico: '))
n2 = int(input('Outro valor numérico ')) 
s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1**n2
print('A sima é {}, \n o produto é {} e a divisão é {:.3f}'.format(s,m,d), end=' ')
print('Divisão inteira {} e potência {}'.format(di,e))





