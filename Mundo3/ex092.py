# CADASTRO DE TRABALHADOR # 
from datetime import date 

cadastro = dict()

cadastro['Nome'] = str(input('Digite o nome: ')).strip() 
cadastro['Idade'] = date.today().year - int(input('Digite o ano de nascimento: ')) 
cadastro['CTPS'] = int(input('Carteira de Trabalho [0 não tem]: ')) 

if cadastro['CTPS'] != 0: 
    cadastro['Ano de contrato'] = int(input('Ano de contrato: ')) 
    cadastro['Salário'] = float(input('Salário (R$): ')) 
    cadastro['Aposentadoria'] = (cadastro['Ano de contrato'] + 35) - date.today().year + cadastro['Idade']

print('-'*40)
for k, v in cadastro.items(): 
    print(f'{k}: {v}')