# TUPLA DE PRODUTOS E PREÇOS # 
produtos = ('Notebook', 2500, 'Monitor', 3700, 'Livro', 37.50, 'Drone', 289.99, 'Ingresso', 40) 
pular = False
print("-" * 30) 
print("LISTA DE PREÇO DOS PRODUTOS")
print("-" * 30)
print("NOME                    PREÇO\n")

for x in produtos: 
    if type(x) == str:
        print(f"{x:.<24}", end='') 

    else:
        print(f"R${x:.2f}", end='')
        pular = True
    
    if pular == True: 
        print("\n") 
        pular = False