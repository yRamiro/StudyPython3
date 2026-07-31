# BOLETIM COM LISTAS COMPOSTAS # 
# LER DUAS NOTAS (OK) | MOSTRAR BOLETIM (OK) | INDIVIDUAL (OK)

dados = list() 
n = 0
continuar = 'S' 

while continuar == 'S': 
    dados.append([]) 
    dados[n].append(str(input("Digite o nome: ")))
    dados[n].append(float(input("Digite a nota 1: "))) 
    dados[n].append(float(input("Digite a nota 2: "))) 

    continuar = str(input("Deseja continuar registrando alunos [S/N]? ")).upper().strip()
    while continuar != 'S' and continuar != 'N':
        continuar = str(input("Por favor, insira uma opção válida [S/N]: ")).upper().strip() 

    if continuar == 'N': 
        break 

    else: 
        n += 1

print('-' * 35) 
print(f"{'Nº':<4} | {'NOME':<15} | {'MÉDIA':>7}")
print('-' * 35)

for i, aluno in enumerate(dados): 
    media = (aluno[1] + aluno[2]) / 2
    print(f"{i:<4} | {aluno[0]:<15} | {media:>7.1f}")

print('-' * 35) 
while True: 
    individual = int(input("Deseja ver as notas de algum aluno? [999 para sair] ")) 
    if individual == 999: 
        break

    if 0 <= individual < len(dados): 
        print('-' * 35) 
        print(f"{'NOME':<15} | {'NOTA 1':<10} | {'NOTA 2':>10}")
        print(f"{dados[individual][0]:<15} | {dados[individual][1]:<10} | {dados[individual][2]:>10}") 

    else: 
        print(f"Digite um nº de aluno válido! (0 - {len(dados) - 1}) ") 

# O JEITO IDEAL DE SER FEITO SERIA COM 3 INPUTS PARA A LISTA: 
# nome = str(input("Digite o nome: ")) 
# nota1 = float(input("Digite a nota 1: ")) 
# nota2 = float(input("Digite a nota 2: ")) 
# media = (nota1 + nota2) / 2
# dados.append([nome, [nota1, nota2], media]) 
    # DESSA FORMA, A ESTRUTURA FICA EXATAMENTE COMO O PROFESSOR PEDIU: 1 LISTA MACRO, E 2 LISTAS EMBUTIDAS.