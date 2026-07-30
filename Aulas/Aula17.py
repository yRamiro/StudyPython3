# ANOTAÇÕES DA AULA 17 #  
lanche = ['Hamburguer', 'Suco', 'Pizza', 'Picolé'] 
print(lanche)

lanche.append('Cookie') # no final, insira 'Cookie' 
print(lanche)

lanche.insert(0, 'Cachorro Quente') # na posição 0, insira 'Cachorro Quente'
print(lanche) 

del lanche[3] # remoção por casa pt1
print(lanche) 

lanche.pop(2) # remoção por casa pt2
print(lanche) 

lanche.remove('Picolé') # remoção pelo conteúdo
print(lanche) 

if 'Cachorro Quente' in lanche: # remoção de conteúdo com uma condicional
    lanche.remove('Cachorro Quente') 
    print(lanche) 


valores = [6, 4, 5, 2, 3, 1] 
print(valores) 

valores.sort() # organiza os valores
print(valores) 

valores.sort(reverse=True) # ordem contrária
print(valores)

seq = list(range(1, 7)) # cria um variável já organizada
print(seq)

a = [2, 3, 4, 7] 
b = a 
b[2] = 8 
print(f'Lista A: {a}') 
print(f'Lista B: {b}') 

a = [2, 3, 4, 7] 
b = a[:] 
b[2] = 8 
print(f'Lista A: {a}') 
print(f'Lista B: {b}') 
