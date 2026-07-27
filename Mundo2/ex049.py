# TABUADA V2.0 # 
num = int(input("Digite um número: ")) 
print("A seguir, a tabuada deste número: ") 
for c in range(1, 11): 
    result = num*c
    print(f"{num} x {c} = {result}")