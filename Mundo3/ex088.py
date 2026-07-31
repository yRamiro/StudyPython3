# PALPITES PARA A MEGA SENA #

from random import randint

print('-'*40) 
print("PALPITADOR DA MEGA SENA".center(40)) 
print('-'*40) 

matriz = list() 
n = int(input("Quantos jogos você quer que eu palpite? ")) 
while n <= 0: 
    n = int(input("Mínimo de 1 jogo! ")) 

for x in range(0, n):
    matriz.append([]) 

for palp in range(0, n):
    for x in range(0, 6):
        num = randint(1, 60) 
        while num in matriz[palp]: 
            num = randint(1, 60)
        
        if num not in matriz[palp]: 
            matriz[palp].append(num)   
    
    matriz[palp].sort()
    print(f"Palpite para o {palp + 1}º jogo: {matriz[palp]}") 

print("Boa sorte!")