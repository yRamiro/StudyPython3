# CADASTRO DE PESSOAS PARA O EXERCÍCIO 115 #
from time import sleep

def cadastrar(): 
    print('-'*40) 
    print(f'\033[34m{"CADASTRAR UM PESSOA":^40}\033[0m') 
    print('-'*40)
    sleep(2)

    try:
        nome = str(input('Digite o nome: ')) 

    except KeyboardInterrupt: 
        print('\nO usuário não quis informar o nome')
        nome = 'Desconhecido'

    try:
        idade = int(input('Digite a idade: '))

    except KeyboardInterrupt: 
        print('\nO usuário não quis informar a idade') 
        idade = 0

    with open("/home/g-ramiro/Desktop/CursoPython3/Mundo3/sistemaCad/registros.txt", "a", encoding='utf-8') as arquivo:
        arquivo.write(f'{nome:<20}            {idade} anos\n')  

    print()
    print('Cadastrando...') 
    sleep(2)