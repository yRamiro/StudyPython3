# JOGO DE DADOS # 

from random import randint 
 
jogos = {'Jogador 1': 0, 
'Jogador 2': 0, 
'Jogador 3': 0, 
'Jogador 4': 0} 

for k in jogos.keys(): 
    num = randint(1,6)
    jogos[k] = num
    print(f"{k} tirou {num}")

jogos_ordenados = dict(sorted(jogos.items(), key =lambda item: item[1], reverse=True))
# DESTRINCHAMENTO: 
 # lambda é uma criação de função rápida para casos únicos
 # -> jogos.items() transforma o dicionário jogos em uma tupla; 
 # sorted() é uma função padrão de ordenamento
 # -> key = lambda item: item[1]: basicamente o key (chave) conversa para o sorted() pegue somente os valores apresentados em item[1] (item[0] seria o nome) 
 # reverse=True, no final, ao pegar todos os item[1], organize os (sorted()) em função decrescente

r = 0

print('-'*30) 
print('RANKING DOS JOGADORES') 
print('-'*30)
for k, v in jogos_ordenados.items(): 
    r += 1
    print(f'{r}º Lugar: {k} com {v}') 

# ANOTAÇÃO FINAL: 
# NA RESOLUÇÃO DO PROFESSOR GUANABARA, ELE IMPORTOU UMA NOVA BIBLIOTECA: 
# from operator import itemgetter 
# e usou: 
# ranking = sorted(jogos.tems(), key=itemgetter(1), reverse=True) 
#FAZ A MESMA COISA QUE A LINHA UTILIZADA POR MIM NESTE CÓDIGO, MAS DE UMA FORMA MAIS SIMPLES E SEM USAR FUNÇÃO DIRETAMENTE (QUE AINDA NÃO FOI ENSINADO NO CURSO)