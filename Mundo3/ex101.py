# FUNÇÕES PARA VOTAÇÃO # 
from datetime import date 

print('='*40)
ano = int(input('Em que ano você nasceu? ')) 

def votação(ano): 
    idade = date.today().year - ano
    
    if idade < 16: 
        return(f'Com {idade} anos: Seu VOTO É NEGADO!')

    elif 16 <= idade < 18 or idade > 70: 
        return(f'Com {idade} anos: Seu VOTO É OPCIONAL!') 

    else: 
        return(f'Com {idade} anos: Seu VOTO É OBRIGATÓRIO!') 

print(votação(ano))