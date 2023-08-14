# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:  -Até 9anos:MIRIM   -Até 14anos:INFANTIL   -Até19anos:JUNIOR  -Até 20anos:SÊNIOR  -Acima:MASTER
idade = int(input('Digite sua idade: '))
if idade < 9:
    print('Mirim')
elif 9 <= idade and idade < 14:
    print('Infantil')
elif 14 <= idade and idade < 19:
    print('Junior')
elif 19 <= idade and idade < 20:
    print('Sênior')
else:
    print('MASTER')
    pass