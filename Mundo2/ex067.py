# TABUADA V3.0 # 
num = 0 
while num >= 0: 
    num = int(input("Digite um número que deseja visualizar a tabuada [digite um número negativo para sair]: ")) 
    
    if num < 0: 
        print("Até mais!") 
        break
    
    else: 
        for c in range(1, 11): 
            print(f"{num} x {c} = {num*c}") 