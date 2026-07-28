# PAR OU ÍMPAR # 
import random
num = numPC = pcWin = cont = resultado = 0 
escolha = "" 

while pcWin == 0: 
    num = int(input("Escolha um número: ")) 
    numPC = random.randint(1, 10) 
    resultado = num + numPC
    escolha = str(input("O computador sorteou um número. A soma entre os números será par ou ímpar [P/I]? ")).upper().strip() 

    if resultado % 2 == 0 and escolha == 'P': 
        print(f"Parabéns, você acertou!\nA soma resultou em {resultado}. Jogue novamente!") 
        cont += 1

    elif resultado % 2 == 1 and escolha == 'I': 
        print(f"Parabéns, você acertou!\nA soma resultou em {resultado}. Jogue novamente!")
        cont += 1

    else: 
        pcWin = 1 
        break 

if pcWin == 1: 
    print(f"Que pena, você perdeu depois de uma sequência de {cont} acerto(s).")