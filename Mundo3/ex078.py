# MAIOR E MENOR NA LISTA # 
valores = list() 
maior = menor = 0

for v in range(1, 6): 
    valores = int(input("Digite um número: ")) 
    if v == 1: 
        maior = valores 
        menor = valores 

    else: 
        if valores > maior: 
            maior = valores 

        elif valores < menor: 
            menor = valores 

print(f"O maior valor digitado foi {maior} e menor foi {menor}")
