# FUNÇÕES APROFUNDADAS EM PYTHON # 

def leiaInteiro(txt): 
    try:
        while True: 
            n = input(txt) 
            try: 
                n = int(n) 
                return n 

            except (ValueError, TypeError): 
                print('\033[31mERRO! Digite um número INTEIRO!\033[m')

    except KeyboardInterrupt: 
        print("\nO usuário não quis digitar o número.")
        return 0


def leiaFloat(txt): 
    try:
        while True: 
            n = input(txt) 
            try: 
                n = float(n) 
                return n 

            except (ValueError, TypeError): 
                print('\033[31mERRO! Digite um número REAL!\033[m') 

    except KeyboardInterrupt: 
        print("\nO usuário não quis digitar o número.")
        return 0

i = leiaInteiro('Digite um número INTEIRO:') 
f = leiaFloat('Digite um número REAL:') 
print(f'O número inteiro digitado foi {i} e o número real digitado foi {f}')