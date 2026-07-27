# SOMA DOS PARES #  
soma = 0 
contPar = 0
for c in range(0, 6): 
    num = int(input("Digite um número: ")) 
    if num % 2 == 0: 
        contPar = contPar + 1
        soma = soma + num 
print(f"De 6 números, foram digitados {contPar} números pares e a soma entre eles é: {soma}")