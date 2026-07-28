# MAIOR, MENOR E MÉDIA # 
maior = menor = soma = cont = 0 
controle = 1 
while controle != 0: 
    num = int(input("Digite um numero qualquer: ")) 
    
    if cont == 0: 
        maior = num 
        menor = num
    else: 
        if num > maior: 
            maior = num 

        elif num < menor: 
            menor = num 
    soma += num 
    cont += 1 

    controle = int(input("Deseja continuar inserindo valores?\n1 - Sim\n0 - Não\n")) 

if controle == 0: 
    print(f"O maior número digitado foi: {maior}\nO menor número digitado foi: {menor}\nA média dos números digitados foi: {(soma/cont):.2f}")