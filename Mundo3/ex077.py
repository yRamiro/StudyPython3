# TUPLA COM VOGAIS # 
palavras = ('Rico', 'dinheiro', 'aprender', 'estudar', 'programador', 'futuro', 'defesa', 'drone', 'familia') 
for x in palavras: 
    print(f"As vogais da palavra {x.upper()} são: ", end='') 
    for letra in x: 
        if letra.upper() in 'AEIOU':
            print(letra, end=' ')  

    print("\n")