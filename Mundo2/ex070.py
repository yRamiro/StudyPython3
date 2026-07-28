# ANÁLISE DE PRODUTOS # 
total = valor = produtos1000 = valorBarato = 0 
contador = 1
produto = nomeBarato = controle = '' 
while controle != 'N': 
    produto = str(input(f"Informe o nome do produto {contador}: ")) 
    valor = float(input(f"Informe o preço do produto {contador}: ")) 
    while valor < 0: 
        valor = float(input(f"Informe um preço válido para o produto {contador}: "))

    if contador == 1: 
        nomeBarato = produto 
        valorBarato = valor 

    else: 
        if valor < valorBarato: 
            nomeBarato = produto 
            valorBarato = valor 

    if valor > 1000: 
        produtos1000 += 1
    
    total += valor 

    controle = str(input("Deseja registrar mais produtos? [S/N] ")).upper().strip() 
    while controle != 'S' and controle != 'N': 
        controle = str(input("Deseja registrar mais produtos? [S/N] ")).upper().strip() 

    if controle == 'N': 
        break 

    else: 
        contador += 1 

if controle == 'N': 
    print(f"{contador} produto(s) registrados:") 
    print(f"Total gasto: R${total:.2f}") 
    print(f"{produtos1000} produto(s) acima de R$1000") 
    print(f"O produto mais barato foi a/o {nomeBarato}, custando R${valorBarato}")