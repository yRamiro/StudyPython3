# VALORES UNÍCOS EM UMA LISTA # 
valores = list() 
escolha = ''
continuar = igual = True

while continuar: 
    num = int(input("Digite um número: ")) 
    while num in valores:
        num = int(input("OPS! Parece que você ja digitou esse valor. Tente outro: ")) 
        
    valores.append(num)
    
    escolha = str(input("Deseja inserir mais números? [S/N] ")).upper().strip()
    while escolha != 'S' and escolha != 'N': 
        escolha = str(input("Digite uma opção válida [S/N]: ")) 
    
    if escolha == 'S': 
        continaur = True 
        igual = True

    else: 
        continuar = False 
        break 

valores.sort() 
print(f"Os valores digitados em ordem crescente: {valores} ") 
