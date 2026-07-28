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
        resultado = resultado * (aux*(aux-1)) 
        aux = aux - 2 
    print(f"O fatorial de {num} é {resultado}.")