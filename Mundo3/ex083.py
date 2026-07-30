# EXPRESSÕES VÁLIDAS # 
    # FEITA COM AJUDA DA RESOLUÇÃO DO PROFESSOR # 
guardar = list() 

expressao = str(input("Digite uma expressão matemática para válidação: ")) 

for x in expressao: 
    for j in x: 
        if j == '(': 
            guardar.append(j)

        elif j == ')': 
            if len(guardar) > 0: 
                guardar.pop() # remove o último elemento 

            else: 
                guardar.append(j) 
                break 

if len(guardar) > 0: 
    print("Expressão inválida!") 

else: 
    print("Expressão válida!")