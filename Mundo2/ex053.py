# PALÍNDROMO #
palindromo = 0
frase = str(input("Digite uma frase: ")).upper()
nova_frase = frase.replace(" ", "")
tamanho = len(nova_frase)
x = tamanho - 1 
for c in range(tamanho):
    if nova_frase[c] != nova_frase[x]:
        palindromo = 1 
    x = x - 1
if palindromo == 0: 
    print("A frase digitada é um palíndromo!") 
else: 
    print("A frase digitada não é um palíndromo!")