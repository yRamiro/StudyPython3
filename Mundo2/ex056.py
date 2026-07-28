# ANALISADOR # 
soma_idade = 0  
nomeHomem = " "
idadeHomem = 0 
idadeMulher = 0 
for c in range(1, 5): 
    nome = str(input(f"Pessoa {c}, qual o seu nome? ")) 
    idade = int(input(f"Pessoa {c}, qual a sua idade? ")) 
    genero = str(input(f"Pessoa {c}, quaal o seu genêro (Homem/Mulher)? ")).lower() 
    
    if idade < 20 and genero == "mulher": 
        idadeMulher += 1 

    elif genero == "homem" and idade > idadeHomem: 
        idadeHomem = idade
        nomeHomem = nome 

    soma_idade += idade 

print(f"Neste grupo: \n {nomeHomem} é o nome do homem mais velho \n Há {idadeMulher} mulher(es) com menos de 20 anos \n {soma_idade/4} é a idade média do grupo." ) 