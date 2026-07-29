# TABELA BRASILEIRÃO # 
tabela = ('Palmeiras', 'Flamengo', 'Athletico-PR', 'Fluminense', 'Bragantino', 'Bahia', 'Botafogo', 'Atlético-MG', 'Corinthians', 'Coritiba', 'Cruzeiro', 'São Paulo', 'Vitória', 'Santos', 'Grêmio', 'Internacional', 'Vasco', 'Remo', 'Mirassol', 'Chapecoense') 

cincoP = tabela[:5] 
quatroU = tabela[16:]
alfa = sorted(tabela)

chape = 0 
for pos, x in enumerate(tabela): 
    if x == 'Chapecoense': 
        chape = pos + 1

print("Tabela do Brasileirão: ") 
print(f"Os cinco primeiro colocados: {cincoP}") 
print(f"O grupo do rebaixamento: {quatroU}") 
print(f"A tabela em ordem alfabética: {alfa}") 
print(f"A Chapecoense está na posição {chape}")