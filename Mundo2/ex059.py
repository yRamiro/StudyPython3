# MENU DE OPÇÕES # 
num1 = num2 = 0 
escolha = 0 
num1 = int(input("Digite um número: ")) 
num2 = int(input("Digite o mesmo ou outro número: ")) 

while escolha != 5: 
    escolha = int(input("Escolha uma opção:\n[1] - Somar\n[2] - Multiplicar\n[3] - Maior número\n[4] - Novos números\n[5] - Sair\n")) 

    if escolha == 1:
        print(f"A soma entre os números é: {num1 + num2}") 

    elif escolha == 2: 
        print(f"O produto dos números é: {num1*num2}") 

    elif escolha == 3: 
        if num1 > num2: 
            print(f"O número {num1} é maior que o número {num2}!") 

        elif num2 > num1: 
            print(f"O número {num2} é maior que o número {num1}!") 

        elif num1 == num2: 
            print("Os números são iguais!") 

    elif escolha == 4: 
        num1 = int(input("Digite um número: ")) 
        num2 = int(input("Digite o mesmo ou outro número: ")) 

if escolha == 5: 
    print("Até mais!")