# FICHA DO JOGADOR # 
def ficha(nome, gols):
    if len(nome) == 0: 
        nome = '<desconhecido>' 

    if len(gols) == 0: 
        gols = '0'
    
    return f'O jogador {nome} fez {gols} gol(s)!' 

print("="*40)
nome = str(input('Qual o nome do jogador? ')).strip()
gols = str(input('Quantos gol(s) o jogador fez? ')).strip() 
print(ficha(nome, gols)) 