# Funções para sortear e somar

from random import randint
from time import sleep

lista = [] 

def sortear(lista): 
    print('='*40)
    print('Sorteando números...')
    for c in range(0, 5): 
        lista.append(randint(1, 50)) 
        
    for num in lista: 
        print(num, end= ' ', flush=True) 
        sleep(0.5)    
    print()


def somaPar(lista): 
    print('-'*30)
    print('Números pares encontrados na lista: ', end='')
    soma = cont =  0
    for num in lista: 
        if num % 2 == 0: 
            print(num, end=' ')
            soma += num 
            cont +=1 
    print() 
    print(f'Foram encontrados {cont} números pares. A soma entre eles resulta em: {soma}') 
    print('<<<PROGRAMA ENCERRADO>>>')

sortear(lista) 
somaPar(lista)