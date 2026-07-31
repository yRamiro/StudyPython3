pessoas = [['Pedro', 25], ['Ramiro', 19], ['Leticia', 32]] 
print(pessoas[0][0]) 
print(pessoas[1][1]) 
print(pessoas[2][0])
print(pessoas[1]) 

galera = [['João', 19], ['Ana', 32], ['Joaquim', 13], ['Maria', 45]]
print(galera[3][0]) # MARIA 
for p in galera: 
    print(f'{p[0]} tem {p[1]} anos') 

pessoal = list() 
dados = list() 
for c in range(0, 3): 
    dados.append(str(input("Nome: "))) 
    dados.append(int(input("Idade: "))) 
    pessoal.append(dados[:]) 
    dados.clear() 

for x in pessoal: 
    if x[1] > 21: 
        print(x[0]) 