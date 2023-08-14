'''

Variáveis Compostas (Dicionários)

02/12/2021

Exercicios: 90 a 
'''

"""
dados = dict()

dados = {'nome':'Pedro', 'idade':25}
print(dados[nome]) # Pedro
print(dados[idade]) # 25

dados['sexo'] = 'M'
del dados['idade']

filme = {'titulo':"Star Wars", 'ano':1977, 'diretor':'George Lucas'}
print(filme.values())
print(filme.keys())
print(filme.items())

for k,v in filme.items():
    print(f"O {k} é {v}")

locadora = [{'titulo':"Star Wars", 'ano':1977, 'diretor':'George Lucas'}, {'titulo':"Avangers", 'ano':2012, 'diretor':'Joss Whedon'}, {'titulo':"Matriz", 'ano':1999, 'diretor':'Wachowski'}]

print(locadora[0]['ano']) # 1977
print(locadora[2]['titulo']) # Matrix

"""

pessoas = {'nome':'Gustavo', 'sexo':'M', 'idade':22}
print(f"O {pessoas['nome']} tem {pessoas['idade']} anos.")
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

del pessoas['sexo']
pessoas['nome'] = 'Leandro'
pessoas['peso'] = 98.5
for k,v in pessoas.items():
    print(f'{k} = {v}')


brasil = []
estado1 = {'uf':'Rio de Janeiro', 'sigla':'RJ'}
estado2 = {'uf':'Sao Paulo', 'sigla':'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil)
print(brasil[0])
print(brasil[0]['uf'])
print(brasil[1]['sigla'])

estado = dict()
brasil = list()

for c in range(3):
    estado['uf'] = input("Unidade Fedetativa: ")
    estado['sigla'] = input("Sigla do Estado: ")
    brasil.append(estado.copy())
print(brasil)
for e in brasil:
    #print(e)
    for k,v in e.items():
        #print(f"O campo {k} tem valor {v}.")
        print(v, end=" ")
    print()




