# FUNÇÃO PARA FATORIAL #

def fatorial(num, show=False): 
    """-> Calcula o fatorial de um número. 
    :parâmetro num: O número a ser calculado; 
    :parâmetro show: Mostrar ou não a conta (opcional)
    :return: Retorna o fatorial de num.
    """  
    print('-'*40)
    facto = 1
    
    if show == False:
        for c in range(num, 0, -1): 
            facto = facto * c 
        return facto 

    else :
        for c in range(num, 0, -1): 
            facto = facto * c 
            
            if c != 1:
                print(f'{c} x', end=' ')
            
            else: 
                print(f'{c} =', end=' ') 
        return facto
        print() 

# help(fatorial) 
print(fatorial(5, show=True))