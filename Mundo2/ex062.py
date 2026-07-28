# PROGRESSÃO ARITMÉTICA V3.0) 
termo = int(input("Digite o primeiro termo da sua PA: ")) 
razao = int(input("Digite a razão da sua PA: ")) 
cont = 1  
controle = 1

print("\nEis os 10 primeiros termos da sua PA:")
while cont < 11: 
    print(termo, end=' ') 
    termo += razao 
    cont += 1  

while controle != 0:
    novosTermos = int(input("\nDeseja ver mais quantos termos da sua PA? ")) 
    controle = novosTermos
    if novosTermos != 0:
        cont = 1
        while cont < novosTermos+1: 
            print(termo, end=' ') 
            termo += razao 
            cont += 1

if controle == 0: 
    print("\nAté mais!")