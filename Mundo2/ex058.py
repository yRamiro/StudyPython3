# ADVINHAÇÃO V2.0 # 
import random 
n = random.randint(0, 10) 
num = int(input("Pensei em número de 0 a 10. Consegue advinhar? ")) 
palpites = 1 

if num == n: 
    print(f"Parabéns você acertou de primeira!") 

else: 
    while num != n: 
        num = int(input("Errou! Tente novamente: ")) 
        palpites += 1 

    if num == n: 
        print(f"Parabéns! Você acertou com {palpites} tentativas!")