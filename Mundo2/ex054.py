# GRUPO DA MAIORIDADE # 
maior = 0 
menor = 0
for c in range(1, 8): 
    ano = int(input(f"Pessoa {c}, digite seu ano de nascimento: ")) 
    if 2026 - ano >= 18: 
        maior += 1 
    else: 
        menor += 1 
print(f"Do grupo, {maior} pessoas são maiores de idade e {menor} são menores de idade.") 