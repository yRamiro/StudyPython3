# INTERACTIVE HELPING SYSTEM IN PYTHON # 

from time import sleep

def ajuda(txt): 
    print("\033[1;30;44m")
    print('-'*40) 
    print(f'Iniciando ajuda para {txt}...') 
    print('-'*40 + "\033[0m")
    
    sleep(3)

    print("\033[0;30;47m")
    help(txt) 
    print("\033[0m")

while True: 
    print("\033[1;30;42m") 
    print('=' * 40)
    print('Sistema de Ajuda')
    print('=' * 40 + "\033[0m" )
    txt = str(input('Digite a função ou biblioteca> ')).strip().lower()
    if txt == 'fim': 
        print("\033[1;30;47m") 
        print('=-'*40)
        print("Até logo!") 
        print('=-'*40 + "\033[0m")     
        
        break  

    else: 
        ajuda(txt)