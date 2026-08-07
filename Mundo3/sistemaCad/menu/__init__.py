# MENU PARA O EXERCÍCIO 115 # 

def menuPrincipal(): 
    print('='*40) 
    print(f'\033[34m{"MENU PRINCIPAL":^40}\033[0m') 
    print('='*40) 
    print('\033[33m1 - Ver pessoas cadastradas\n2 - Cadastrar nova pessoa\n3 - Sair do sistema\033[0m') 
    while True:
        try:
            op = int(input('Sua opção > ')) 

        except(TypeError, ValueError): 
            print('\033[31mERRO! Digite um número INTEIRO válido!\033[m') 

        except KeyboardInterrupt: 
            print('\n\033[35mO usuário optou por cancelar a execução do sistema...\033[0m') 
            return 3

        if op > 3 or op < 1: 
            print('\033[31mERRO! Digite uma opção VÁLIDA (1 - 3)!\033[m') 

        else: 
            return op