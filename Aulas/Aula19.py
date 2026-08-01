# DICIONÁRIOS {} # 
dados = dict() 
dados={'nome': 'Pedro', 'idade': 25} 
print(dados['nome']) 
print(dados['idade']) 
dados['sexo'] ='M' # NÃO PRECISA DE APPEND PARA ADICIONAR EM DICIONÁRIOS 
print(dados['sexo']) 
del dados['idade'] 
print(dados) 

filme = {'título': 'Star Wars', 
'ano': 1977, 
'diretor': 'George Lucas'
} 

print(filme.values()) # VALORES: 'Star Wars', 1977, 'George Lucas' 
print(filme.keys()) # KEYS: 'título', 'ano', 'diretor'
print(filme.items()) # ITEMS: VALORES E KEYS 

for k, v in filme.items(): 
    print(f'O {k} é {v}') 

# LOCADORA 
locadora = list() 
filmes = {'título': 'Star Wars', 
'ano': 1977, 
'diretor': 'George Lucas'
}  

locadora.append(filmes.copy()) 

filmes.update({'título': 'Avengers'}) 
filmes.update({'ano': 2012}) 
filmes.update({'diretor': 'Joss Whedon' })

locadora.append(filmes.copy())

print(locadora)

for k, v in filmes.items(): 
    print(f'O {k} é {v}') 

estado = dict() 
brasil = list() 
for c in range(0, 3): 
    estado['uf'] = str(input('Unidade Federativa: ')) 
    estado['sigla'] = str(input('Sigla do estado: ')) 
    brasil.append(estado.copy()) 

for e in brasil:
    for v in e.values():
        print(v, end=' ') 
    print()