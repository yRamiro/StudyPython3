# VISUALIZAÇÃO DE LISTA PARA O EXERCÍCIO 115 #

from time import sleep

def mostrarLista(): 
    print('-'*40) 
    print(f'\033[32m{"CADASTROS":^40}\033[30m') 
    print('-'*40)
    sleep(2)

    with open('/home/g-ramiro/Desktop/CursoPython3/Mundo3/sistemaCad/registros.txt', 'r', encoding='utf-8') as arquivo: 
        conteudo = arquivo.read() 
        print(conteudo)

    sleep(2) 
    print()