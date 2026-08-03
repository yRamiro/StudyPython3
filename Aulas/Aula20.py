# FUNÇÕES 

def mostraLinha():
    print("-"*40) 

mostraLinha() 
print("SISTEMA DE ALUNOS") 
mostraLinha() 

def título(msg): 
    print("-"*30) 
    print(msg) 
    print("-"*30) 

título("   CURSO EM VÍDEO   ") 
título("   APRENDA PYTHON   ")  
título("   GUSTAVO GUANABRA   ") 

def soma(a, b): 
    print(f'A = {a} e B = {b}')
    s = a + b 
    print(s) 

soma(4, 5) 
soma(b=3, a=6) 
soma(90, 9) 

def contador(*num): # O que isso diz ao Python: Vários parâmetros serão passados, todos eles 'empacote' em num
    tam = len(num)
    print(f'Foram passados os valores {num}, ao todo são {tam} números') 

contador(2, 1, 7) 
contador(8, 0) 
contador(4, 4, 7, 6, 2) 


def dobra(valores): 
    for pos, v in enumerate(valores): 
        valores[pos] = v*2  
        

valores = [7 , 3, 4] 
dobra(valores) 
print(valores)