# ANÁLISE DE GRUPO # 
idade = mulher20 = contHomem = contIdade = 0 
registro = 1
sexo = control = '' 
while control != 'N': 
    idade = int(input(f"Pessoa {registro}, qual a sua idade? ")) 
    sexo = str(input(f"Pessoa {registro}, qual o seu sexo? [M/F] ")).upper().strip() 
    while sexo != 'F' and sexo != 'M': 
        sexo = str(input(f"Pessoa {registro}, qual o seu sexo? [M/F] ")).upper().strip() 

    if idade > 18: 
        contIdade += 1

    if sexo == 'M': 
        contHomem += 1 

    if idade < 20 and sexo == 'F': 
        mulher20 += 1 

    control = str(input("Deseja registrar mais pessoas? [S/N] ")).upper().strip() 
    while control != 'S' and control != 'N': 
        control = str(input("Deseja registrar mais pessoas? [S/N] ")).upper().strip()

    if control == 'N': 
        break; 

    else: 
        registro += 1 

if control == 'N': 
    print(f"Foram registrado(s) {registro} pessoa(s)") 
    print(f"No total:\n{contIdade} pessoa(s) com mais de 18 anos\n{contHomem} homem(ns) registrado(s)\n{mulher20} mulher(es) com menos de 20 anos.")