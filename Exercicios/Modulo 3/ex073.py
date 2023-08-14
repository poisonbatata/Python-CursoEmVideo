# Crie uma tabela preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre :  A) Apenas os 5 primeiros colocados   B) Os últimos 4 colocados da tabela   C) Uma lista com os times em ordem alfabética   D) Em que posição na tabela está o time da Chapecoense



times = ('Palmeiras','Santos','Flamengo','Atlético','Internacional','Athletico-PR','Botafogo','Goiás','Corinthians','São Paulo','Grêmio','Bahia','Ceará SC','Fortaleza','Vasco da gama','Cruzeiro','Fluminense','Chapecoense','CSA','Avaí')

print('-='*30)
print(f'A lista dos times é: {times}')
print('-='*30)
print(f'Os 5 primeiros são: {times[0:6]}')
print('-='*30)
print(f'Os 4 últimos são: {times[-4:]}')
print('-='*30)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-='*30)
# O guanabara n ensinou try except ainda, mas decidi usar aqui assim msm
try:
    print(f' O time da Chapecoense está na {times.index("Chapecoense")+1}º posição')
except:
    print('O time da Chapecoense não está na lista!')
