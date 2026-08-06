# MATERIAL DOS EXERCÍCIOS 107, 108, 109, 110, 111, 112 # 
def moeda(n, moeda='R$'): 
    return f'{moeda}{n:.2f}'.replace('.', ',')

def metade(n=0, format=False): 
    result = n/2

    if format == True: 
        return moeda(result)

    else:
        return result


def dobro(n=0, format=False): 
    result = n*2

    if format == True: 
        return moeda(result)

    else:
        return result


def aumentar(n=0, taxa=0, format=False): 
    result = n + (n * taxa/100)

    if format == True: 
        return moeda(result)

    else:
        return result 


def diminuir(n=0, taxa=0, format=False): 
    result = n - (n * taxa/100)

    if format == True: 
        return moeda(result)

    else:
        return result 

def resumo(n, taxaA=0, taxaD= 0): 
    print('='*30) 
    print(f'{"RESUMO DA OPERAÇÃO":^30}')
    print('='*30) 
    print(f'Preço analisado:    {moeda(n)}') 
    print(f'Dobro do preço:     {dobro(n, True)}') 
    print(f'Metade do preço:    {metade(n, True)}') 
    print(f'{taxaA}% de aumento:     {aumentar(n, taxaA, True)}') 
    print(f'{taxaD}% de desconto:    {diminuir(n, taxaD, True)}')