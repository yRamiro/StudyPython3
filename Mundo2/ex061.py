# PROGRESSÃO ARITMÉTICA V2.0) 
termo = int(input("Digite o primeiro termo da sua PA: ")) 
razao = int(input("Digite a razão da sua PA: ")) 
cont = 1 

print("\nEis os 10 primeiros termos da sua PA:")
while cont < 11: 
    print(termo, end=' ') 
    termo += razao 
    cont += 1  
if cont == 11: 
    print("\n")