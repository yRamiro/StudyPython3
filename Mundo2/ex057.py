# VALIDAÇÃO DE DADOS #
genero = "" 

while genero != "M" and genero != "F": 
    genero = str(input("Qual o seu gênero? [M/F] ")).upper()
   
if genero == "M": 
    print("Você é um homem!") 
    
elif genero == "F": 
    print("Você é uma mulher!") 