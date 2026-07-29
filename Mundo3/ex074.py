# TUPLA ALEATÓRIA # 
from random import randint 
maior = menor = 0 
num = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10),) 
for pos, x in enumerate(num):  
    if pos == 0: 
        menor = x 
        maior = x
    
    else: 
        if x > maior: 
            maior = x 

        elif x < menor: 
            menor = x

print(f"Os números sorteados foram {num}") 
print(f"O maior número sorteado foi {maior} e menor foi {menor}")    