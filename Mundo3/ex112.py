# ENTRADA DE DADOS MONETÁRIOS #

from utilidadesCeV import dado 
from utilidadesCeV import moeda
m = dado.leiaDinheiro('Digite um preço: R$')
moeda.resumo(m, 80, 35)