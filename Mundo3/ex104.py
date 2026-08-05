# VALIDANDO ENTRADA DE DADOS EM PYTHON # 
    # FEITO COM AUXÍLIO DA RESOLUÇÃO #
def leiaInt(txt):  
    valido = False
    num = 0 
    while True:
        n = str(input(txt))

        if n.isnumeric(): 
            valor = int(n) 
            valido = True
            return valor 
        
        else: 
            print('\033[31mERRO! DIGITE UM NÚMERO INTEIRO VÁLIDO!\033[m')

# Programa princial 
n = leiaInt('Digite um número INTEIRO: ')
print(f'Você acabou de digitar o número {n}!') 
