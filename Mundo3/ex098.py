# FUNÇÃO DE CONTADOR # 

from time import sleep

def contador(inicio, fim, passo): 
    print('='*30)
    
    if passo == 0:
        passo = 1
    
    if inicio < fim: 
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}:')
        fim = fim + 1 
    
        for c in range(inicio, fim, passo): 
            print(c, end=' ', flush=True) 
            sleep(1)

    elif inicio > fim: 
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}:')
        fim = fim - 1
        
        if passo > 0: 
            passo = passo*-1

        for c in range(inicio, fim, passo): 
            print(c, end=' ', flush=True) 
            sleep(1)

    print()

contador(1, 10, 1) 
contador(10, 0, -2) 

i = int(input('Digite o número que sua contagem começa: ')) 
f = int(input('Digite o número em que termina: ')) 
p = int(input('Digite o pulo de casas (1 em 1, 2 em 2): ')) 
contador(i, f, p)