# MAIOR E MENOR PESO #  
maior = 0 
menor = 0 
for c in range(1, 6): 
    peso = int(input(f"Pessoa {c}, qual o seu peso em kg? ")) 
    if c == 1: 
        maior = peso 
        menor = peso 
    else: 
        if peso > maior:
            maior = peso 
        elif peso < menor: 
            menor = peso 
print(f"O maior peso registrado foi {maior}KG e menor peso registrado foi {menor}KG.")