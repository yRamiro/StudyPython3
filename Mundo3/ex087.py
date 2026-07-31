# MAIS SOBRE MATRIZ EM PYTHON # 

somaPar = somaC3 = 0

matriz = [[], [], []] 
for i in range(0, 3): 
    for j in range(0, 3):
        num = int(input(f"Digite um número para a posição [{i}][{j}]: ")) 
        matriz[i].append(num) 
    
for linha, conjunto in enumerate(matriz): 
    for coluna, elemento in enumerate(conjunto): 
        if elemento % 2 == 0: 
            somaPar += elemento 

        if coluna == 2: 
            somaC3 += elemento 

maiorL2 = max(matriz[1])
        
print('-'*40)
print(f"A soma de todos os valores par inseridos é: {somaPar}") 
print(f"A soma dos valores da coluna 3 resulta em: {somaC3}") 
print(f"O maior número da linha 2 é: {maiorL2}")