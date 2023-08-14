# Faça um programa que leia uma frase pelo teclado e mostre : -> Quantas vezes aparece a letra "A"  -> Em qe posição ela aparece a primeira vez. -> Em que posição ela aparece a última vez.
frase = input('Digite uma frase: ').strip().upper()
aparicoes = frase.count('A')
frist = frase.find('A')+1
#last = frase.rfind('A')+1
last = frase[::-1].find('A')
caracteres = len(frase)
last = caracteres - last
print('A letra "A" apareceu em "{}" pela primeira vez em {}, pela ultima em {} e no total {} vezes.'.format(frase,frist,last,aparicoes))