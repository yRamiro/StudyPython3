# FLAG COM BREAK # 
cont = soma = num =  0 
while num != 999: 
    num = int(input("Digite um número qualquer [999 para sair]: ")) 
    
    if num == 999: 
        print(f"Você digitou {cont} números e a soma entre eles é: {soma}")
        break 
    
    else: 
        soma += num 
        cont += 1