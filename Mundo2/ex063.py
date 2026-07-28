# SEQUÊCIA DE FIBONACCI # 

num = int(input("Digite quantos termos deseja ver da sequência de Fibonacci: ")) 
cont = 0 
termo = 0
termoAnt = 0 # termo anteriior 
aux = 0

if num == 0: 
    print("O termo 0 da sequência de Fibonacci é 0")

else: 
    print(f"Eis os {num} primeiro(s) termo(s) da sequência de FIbonacci: ")
    while cont < num: 
        print(termo, end=' ') 
        if termo == 0: 
            termo = 1
        if cont > 0: 
            aux = termo + termoAnt
            termoAnt = termo
            termo = aux
        cont += 1
print("\n")