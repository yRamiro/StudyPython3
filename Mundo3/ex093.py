# CADASTRO DE JOGADOR DE FUTEBOL # 

cadastro = dict() 
gols = list() 

cadastro = {'Nome': '', 
'Gols': gols, 
'Total': 0
}

cadastro['Nome'] = str(input('Digite o nome do jogador: ')).strip() 
partidas = int(input('Quantas partidas o jogador participou? '))

for p in range(0, partidas): 
    gol = int(input(f'Gols na partida {p+1}: '))
    gols.append(gol)
    cadastro['Total'] += gol

print('='*40) 
for k, v in cadastro.items(): 
    print(f'{k}: {v}') 
print('='*40) 
print(f'O jogador {cadastro["Nome"]} jogou {partidas} partidas.') 
for p, g in enumerate(gols): 
    print(f' -> {g} gols na partida {p+1}.') 
print(f'Total de {cadastro["Total"]} gols!')