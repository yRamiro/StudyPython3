# LISTA PARES E ÍMPARES V2.0 # 

valores = [[], []]

for x in range(0, 7): 
    num = (int(input("Digite um número: "))) 
    if num % 2 == 0: 
        valores[0].append(num) 
    
    else: 
        valores[1].append(num) 

valores[0].sort() 
valores[1].sort() 

print('-'*40) 
print(f"Valores pares digitados: {valores[0]}") 
print(f"Valores ímpares digitados: {valores[1]}")