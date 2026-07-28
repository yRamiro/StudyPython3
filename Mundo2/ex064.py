# NÚMEROS COM FLAG # 
num = cont = soma = 0 
while num != 999: 
    num = int(input("Digite um número qualquer [999 para sair]: ")) 
    if num != 999: 
        cont += 1 
        soma += num 
if num == 999: 
    print(f"Você digitiou {cont} número(s) e a soma entre eles resulta em: {soma}") 