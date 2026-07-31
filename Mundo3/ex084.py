# LISTA COMPOSTA E ANÁLISE DE DADOS # 

cadastro = list() 
dados = list() 
leves = list()
pesados =list()
continuar = 'S'
maiorPeso = menorPeso = 0

while continuar == 'S': 
    cadastro.append(str(input("Digite o nome: ")).upper().strip()) 
    cadastro.append(int(input("Digite o peso: "))) 
    dados.append(cadastro[:]) 
    cadastro.clear() 

    continuar = str(input("Deseja cadastrar mais pessoas [S/N]? ")).upper().strip()
    while continuar != 'S' and continuar != 'N': 
        continuar = str(input("Por favor, digite S ou N: ")).upper().strip() 

    if continuar == 'N': 
        break 

for i, x in enumerate(dados): #
    if i == 0: 
        maiorPeso = x[1] 
        menorPeso = x[1]

    else: 
        if x[1] > maiorPeso:
            maiorPeso = x[1] 
        
        elif x[1] < menorPeso: 
            menorPeso = x[1] 

for x in dados: 
    if x[1] == maiorPeso: 
        pesados.append(x[0])

    if x[1] == menorPeso: 
        leves.append(x[0])


print('-'*40) 
print(f"Você cadastrou: {len(dados)} pessoas") 
print(f"O maior peso foi: {pesados} com {maiorPeso}KG") 
print(f"O menor peso foi: {leves} com {menorPeso}KG") 