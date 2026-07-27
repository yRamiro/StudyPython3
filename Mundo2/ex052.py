# NÚMERO PRIMO # 
num = int(input("Digite o número que deseja verificar se é primo ou não: ")) 
div = 0

if num == 0 or num == 1: 
    print("Os números 0 e 1 não podem ser classificados como primos!")

else: 
    for c in range(1, num + 1): 
        if num % c == 0: 
            div += 1 
    if div > 2:
        print(f"O número {num} não é primo!") 
    else: 
        print(f"O número {num} é primo!") 