# DICIONÁRIO EM PYTHON # 
dados = dict()  

nome = str(input("Nome: ")).strip() 
dados.update({'Nome': nome}) 
media = float(input(f"Digite a média de {nome}: ")) 
dados.update({'Média': media})
if media >= 7: 
    dados.update({'Situação': 'aprovado'}) 

elif media >= 5:
    dados.update({'Situação': 'recuperação'})

else: 
    dados.update({'Situação': 'reprovado'})

print('-'*40)
for k, v in dados.items(): 
    print(f'-> {k} é igual a: {v}')