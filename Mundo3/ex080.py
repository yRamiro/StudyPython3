# LISTA SEM SORT # 
valores = list() 
for c in range(0, 5): 
    num = int(input("Digite um número: ")) 
    valores.append(num) 

print(f"Ordem digitada: {valores}")

for i in range(len(valores)): 
    for j in range(i + 1, 5):
        if valores[i] > valores[j]: 
            valores[j], valores[i] = valores[i], valores[j] 

print(f"Os números digitados em ordem crescente: {valores}")