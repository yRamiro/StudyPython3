# ANALISANDO E GERANDO DICIONÁRIOS # 

def notas(*nota, sit=False): 
    if not nota: 
        return {'Quantidade de notas': 0, 'Maior nota': 0, 'Menor nota': 0, 'Media': 0.0}
    
    else:
        valores= {'Quantidade de notas': len(nota), 
        'Maior nota': max(nota), 
        'Menor nota': min(nota), 
        'Media': f'{sum(nota)/len(nota):.2f}'
        }

        if sit == True:
            if sum(nota)/len(nota) >= 7: 
                valores['Situação'] = 'BOA' 
            elif 7 > sum(nota)/len(nota) >= 5 : 
                valores['Situação'] = 'RAZOÁVEL' 
            else: 
                valores['Situação'] = 'RUIM' 

    return print(f'{valores}')

resp = notas(7.8, 7.1, 7.8, sit=True) 