# LISTAS PARES E ÍMPARES # 
valores = list() 
pares = list() 
impares = list()

continuar = True 
while continuar: 
    num = int(input("Digite um número: ")) 
    valores.append(num) 
    
    if num % 2 == 0: 
        pares.append(num) 

    else: 
        impares.append(num)
    
    escolha = str(input("Deseja continuar inserindo números? [S/N]")).upper().strip() 
    while escolha != 'S' and escolha != 'N': 
        escolha = str(input("Insira uma opção válida [S/N]: ")).upper().strip() 

    if escolha == 'N': 
        continuar = False 

print('-'*25) 
print("RELATÓRIO:") 
print('-'*25) 
print(f"Números digitados: {valores}") 
print(f"Números pares digitados: {pares}") 
print(f"Números ímpares digitados: {impares}")