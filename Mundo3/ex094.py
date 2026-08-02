# UNINDO DICIONÁRIOS E LISTAS #  

pessoas = list() 
individuo = dict() 
acimaMedia = list()
mulheres = list()

somaIdade = 0

while True: 
    individuo['Nome'] = str(input('Nome: ')).strip() 
    
    individuo['Sexo'] = str(input('Sexo [M/F]: ')).strip().upper() 
    while individuo['Sexo'] not in 'F, M': 
        individuo['Sexo'] = str(input('Somente [M/F]: ')).strip().upper() 

    if individuo['Sexo'] == 'F': 
        mulheres.append(individuo.copy())

    individuo['Idade'] = int(input('Idade: ')) 
    somaIdade += individuo['Idade']
    
    escolha = str(input('Deseja cadastrar mais pessoas [S/N]? ')).strip().upper() 
    while escolha not in 'S, N': 
        escolha = str(input('Digite uma opção válida [S/N]: ')).strip().upper()

    pessoas.append(individuo.copy()) 
    
    if escolha == 'N': 
        break  

    else: 
        individuo.clear()

for x in range(0, len(pessoas)):
    if pessoas[x]['Idade'] > (somaIdade/len(pessoas)): 
        acimaMedia.append(pessoas[x].copy())

print('='*40) 
print(f'Foram cadastradas {len(pessoas)} pessoas') 
print(f'A média de idade do grupo é: {somaIdade/len(pessoas)} anos') 
print('Mulheres cadastradas: ',end='') 
for v in range(0, len(mulheres)): 
    print(f'{mulheres[v]["Nome"]}', end=' ') 
print()
print('-'*40)
print('Lista de pessoas com a idade acima da média: ') 
for v in acimaMedia: 
    print(f'Nome: {v["Nome"]} | Sexo: {v["Sexo"]} | Idade: {v["Idade"]}')
    