# ANÁLISE DE DADOS EM UMA TUPLA # 

cont9 = pos3 = 0
valid = False

num = (int(input("Digite um número: ")), int(input("Digite um número: ")), int(input("Digite um número: ")), int(input("Digite um número: "))) 


for pos, x in enumerate(num):
    if x == 9: 
        cont9 += 1 

    elif x == 3 and valid == False: 
        pos3 = pos + 1
        valid = True 

print(f"Você digitou os números: {num}")
print(f"O número 9 apareceu {cont9} vez(es)") 
if valid == True:
    print(f"O número 3 apareceu pela primeira vez na posição {pos3}") 

else: 
    print("O número 3 não apareceu!")

print(f"Número(s) par(es) digitado(s):", end=' ')
for x in num: 
    if x % 2 == 0: 
        print(x, end=' ') 
print("\n")