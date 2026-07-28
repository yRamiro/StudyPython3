# FATORAÇÃO# 
resultado = 1
num = int(input("Digite um número para fatorar: ")) 
aux = num

if num < 0: 
    print("Não existe fatorial de números negativos!")

elif num == 0 or num == 1: 
    print(f"O fatorial de {num} é 1. ")

else:
    while (aux-1) > 0: 
        resultado = resultado * aux 
        aux = aux - 1 
    for c in range(num, 0, -1): 
        if c == 1:
            print(c, end='')
        else:
            print(f"{c} x", end=' ') 

    print(f"\nO fatorial de {num} é {resultado}.")