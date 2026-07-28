# CAIXA ELETRÔNICO # 
valorSaque = cont50 = cont20 = cont10 = cont1= 0 
valorSaque = int(input("Bem-vindo ao banco. Qual valor deseja sacar? ")) 
while valorSaque < 0: 
    valorSaque = int(input("Por favor digite um valor válido para sacar: "))
   
while valorSaque > 0: 
        
    cont50 = valorSaque//50 
    valorSaque = valorSaque % 50 
    if valorSaque == 0: 
        break 

    else:
        cont20 = valorSaque//20 
        valorSaque = valorSaque % 20 
        if valorSaque == 0: 
            break 
        
        else:
            cont10 = valorSaque//10 
            valorSaque = valorSaque % 10 
            if valorSaque == 0: 
                break 
        
            else:
                cont1 = valorSaque//1 
                valorSaque = valorSaque%1 
                break 

if valorSaque == 0: 
    print("Cédulas a serem impressas:") 
    print(f"{cont50} cédula(s) de R$50") 
    print(f"{cont20} cédula(s) de R$20")  
    print(f"{cont10} cédula(s) de R$10")  
    print(f"{cont1} moedas(s) de R$1") 