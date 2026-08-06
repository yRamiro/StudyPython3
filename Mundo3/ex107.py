# EXERCITANDO MÓDULOS EM PYTHON # 

from utilidadesCeV import moeda

m = float(input('Digite um preço: R$')) 
print(f'O dobro de R${m} é R${moeda.dobro(m)}') 
print(f'A metade de R${m} é R${moeda.metade(m)}') 
print(f'Com um aumento de 10% em R${m}, temos R${moeda.aumentar(m, 10)}') 
print(f'Com uma redução de 13% em R${m}, temos R${moeda.diminuir(m, 13)}')