# FORMATANDO MOEDAS EM PYTHON PT2 # 

from  utilidadesCeV import moeda

m = float(input('Digite um preço: R$')) 
print(f'O dobro de {moeda.moeda(m)} é {moeda.dobro(m)}') 
print(f'A metade de {moeda.moeda(m)} é {moeda.metade(m, True)}') 
print(f'Com um aumento de 10% em {moeda.moeda(m)}, temos {moeda.aumentar(m, 10, True)}') 
print(f'Com uma redução de 13% em {moeda.moeda(m)}, temos {moeda.diminuir(m, 13, True)}')