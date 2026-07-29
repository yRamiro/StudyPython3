# NÚMERO POR EXTENSO #
sequencia = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treza', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove' 'vinte')

num = int(input("Digite um número de 0 a 20: ")) 

while num < 0 or num > 20: 
    num = int(input("DIgite um número VÁLIDO de 0 a 20: ")) 
    if num > -1 or num < 21: 
        break

print(f"Você digitou o número {sequencia[num]}!")