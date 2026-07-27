# PROGRESSÃO ARITMÉTICA # 
t1 = int(input("Digite o primeiro termo da PA: ")) 
razao = int(input("Digite a razão da PA: ")) 
print("Eis os 10 primeiros termos da sua PA:")
for c in range(t1, t1 + razao*10, razao): 
    print(c, end=' ')