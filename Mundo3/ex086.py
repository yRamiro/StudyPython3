# MATRIZ 3X3 EM PYTHON 
matriz = [[], [], []]
for i in range(0, 3): 
    for j in range(0, 3): 
        num = int(input(f"Digite um número para a posição [{i}][{j}]: ")) 
        matriz[i].append(num)

print('-'*40) 
for pos, i in enumerate(matriz): 
    for j in range(0, 3): 
        print(f"[{matriz[pos][j]:^5}]",end='') 
    print()