# INTERACTIVE HELP 
# help() 
# print(input.__doc__) ou help(input)


# DOCSTRING
def contador(i, f, p): 
    """
    -> FAZ UMA CONTAGEM E MONSTRA NE TELA: 
    :PARÂMETRO i: início da contagem 
    :PARÂMETRO f: fim da contagem 
    :PARÂMETRO p: passos da contagem 
    :return: sem retorno
    EXEMPLO: 
    entrada: contagem (2, 10, 2) 
    saída: 2, 4, 6, 8, 10
    """ 
    c = i
    while c <= f: 
        print(f'{c}', end=' ') 
        c += p 
    print() 
    print("FIM!") 

# Para visualizar o docstring basta digitar -> help(contador) 

# PARÂMETROS OPCIONAIS 
def somar(a=0, b=0, c=0): # Isto é, caso não receba algum valor (a, b ou c) essas atribuições recebem o valor 0.
    soma = a + b + c 
    print(f'A soma vale: {soma}') 

somar(3, 2, 5) 
somar(8, 4) 
somar() 

print('-'*40)

# ESCOPO DE VARIÁVEIS  
# Na programação, escopa é o lugar onde a variável vai existir eonde ela deixa de existir 

a = 5
def teste(b): 
    global a # Desta forma, não é criada uma nova variável 'a'
    a = 8
    b += 4 
    c = 2 
    print(f'A dentro vale {a}') 
    print(f'B dentro vale {b}') 
    print(f'C dentro vale {c}') 

teste(a) 
print(f'A fora vale {a}') 

print('-'*40)

# RETORNO DE VALORES 
def somar(a=0, b=0, c=0): # Isto é, caso não receba algum valor (a, b ou c) essas atribuições recebem o valor 0.
    soma = a + b + c 
    return soma 

r1 = somar(3, 2, 5) 
r2 = somar(1, 7) 
r3 = somar(4) 
print(f'As somas valem {r1}, {r2} e {r3}')