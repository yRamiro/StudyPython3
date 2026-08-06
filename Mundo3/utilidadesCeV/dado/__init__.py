# MÓDULO PARA A LEITURA DE DADOS MONETÁRIOS DO EXERCÍCIO 112 # 
# -> INICIALMENTE, FIZ COM 'n.isnumeric()' mas dessa forma números decimais não são válidados, por utilizei o código abaixo.

def leiaDinheiro(txt): 
    while True: 
        n = input(txt).replace(',', '.')

        try:
            n = float(n) 
            return n
        except ValueError:
            print('\033[31mERRO! Digite um valor monetário válido!\033[m') 