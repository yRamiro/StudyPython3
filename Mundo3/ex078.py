# MAIOR E MENOR NA LISTA # 
valores = list() 
maior = menor = 0

for v in range(1, 6): 
    num = int(input("Digite um número: ")) 
    valores.append(num)
    if v == 1: 
        maior = num 
        menor = num 

    else: 
        if num > maior: 
            maior = num 

        elif num < menor: 
            menor = num 

print(f"Os valores digitados foram: {valores}")
print(f"O maior valor digitado foi {maior} e menor foi {menor}")
