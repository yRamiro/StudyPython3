from sistemaCad import menu 
from sistemaCad import cadastro 
from sistemaCad import lista 

while True:
    m = menu.menuPrincipal() 

    if m == 1: 
        m = lista.mostrarLista() 

    elif m == 2: 
        m = cadastro.cadastrar() 

    else: 
        break 

print(f'\033[35m{"<<<SISTEMA FINALIZADO>>>":^40}\033[0m')