# FORMATANDO MOEDAS EM PYTHON PT1 #

from utilidadesCeV import moeda

m = float(input('Digite um preço: R$')) 
print(f'O dobro de {moeda.moeda(m)} é {moeda.moeda(moeda.dobro(m))}') 
print(f'A metade de {moeda.moeda(m)} é {moeda.moeda(moeda.metade(m))}') 
print(f'Com um aumento de 10% em {moeda.moeda(m)}, temos {moeda.moeda(moeda.aumentar(m, 10))}') 
print(f'Com uma redução de 13% em {moeda.moeda(m)}, temos {moeda.moeda(moeda.diminuir(m, 13))}')