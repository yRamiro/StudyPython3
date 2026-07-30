# DADOS DE UMA LISTA # 
 
continua = True

valores = list() 
while continua: 
    num = int(input("Digite um número: ")) 
    valores.append(num)  
    escolha = str(input("Deseja continuar inserindo valores? [S/N] ")).upper().strip() 
    
    while escolha != 'S' and escolha != 'N': 
        escolha = str(input("Digite uma opção válida [S/N]: ")).upper().strip() 
    
    if escolha == 'N': 
        continua = False 

print("-"*15) 
print("RESUMO DA OPERAÇÃO") 
print("-"*15) 
print(f"Quantidade de números digitados: {len(valores)}") 
valores.sort(reverse=True)
print(f"A ordem decrescente dos números digitados: {valores}") 
if 5 in valores: 
    print("O número 5 foi digitado!") 
else: 
    print("O número 5 não foi digitado!")