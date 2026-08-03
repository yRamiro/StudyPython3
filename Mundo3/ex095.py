# APRIMORANDO OS DICIONÁRIOS # 

jogadores = list()
gols = list() 

cadastro = {'Nome': '', 
'Gols': gols, 
'Total': 0
}

while True:
    cadastro['Nome'] = str(input('Digite o nome do jogador: ')).strip() 
    partidas = int(input('Quantas partidas o jogador participou? '))

    for p in range(0, partidas): 
        gol = int(input(f'Gols na partida {p+1}: '))
        gols.append(gol)
        cadastro['Total'] += gol

    cadastro['Gols'] = gols.copy()
    jogadores.append(cadastro.copy())

    escolha = str(input('Deseja cadastrar mais jogadores? Responda com [S/N]: ')).strip().upper() 
    while escolha not in 'S, N': 
        escolha = str(input('Digite uma opção válida [S/N]: ')).strip().upper()
    
    if escolha == 'N': 
        break

    else: 
        cadastro['Total'] = 0
        gols.clear()

print('='*60) 
print(f"{'COD.':<4} | {'NOME':<14} | {'GOLS':<20} | {'TOTAL':<10}") 
for i, jog in enumerate(jogadores): 
    print(f'{i:<4} | {jog["Nome"]:<14} | {str(jog["Gols"]):<20} | {jog["Total"]:<10}') 

while True: 
    print('-'*60) 
    levantamento = int(input('Deseja levantar os dados de qual jogador? [999 para sair]: ')) 
    while levantamento < 0 or levantamento >= len(jogadores) and levantamento != 999: 
        levantamento = int(input(f'Erro! Digite uma opção válida (0 - {len(jogadores) - 1} ou 999 para sair): '))

    if levantamento == 999: 
        break
    
    else: 
        print(f'Desempenho do jogador {jogadores[levantamento]["Nome"]}:')
        for i, g in enumerate(jogadores[levantamento]['Gols']): 
            print(f'-> {g} gols na partida {i+1}')            


print('<<<PROGRAMA ENCERRADO>>>')    