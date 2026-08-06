# TRATAMENTO DE ERROS E EXCEÇÕES 
""" No Python, temos várias classes de erros: 
---------------------------
2 / 0
ZeroDivisionError: divisão por zero 
---------------------------
r = 2/'2'  
print(r)
TypeError || '2' é uma string e não um número 
---------------------------
lst = [3, 6, 4]
print(lst)
IndexError || Tentativa de acessar uma posição que não existe
--------------------------- 
import uteis 
ModuleNotFoundError || Quando há uma tentativa de importação de um módulo que não foi encontrado 
--------------- 
    E muito mais!
Todos esses erros, são chamados de Exceções

Podemos tratar as exceções com os comandos: 

try -> tente isso 
exccept -> Se der um erro 
else -> Se não der erro
finally -> Finalmente... Executa mesmo se houber certo/falha

""" 

try: 
    x = int(input('Número: '))
    y = int(input('Divisor: '))
    print(x/y) 
except (ValueError, TypeError): 
    print('A variável não é inteira!') 
except ZeroDivisionError: 
    print('Não é possível dividir por zero!')
except KeyboardInterrupt: 
    print('O usuário não quis informar o número')
else: 
    print('Variável inteira!')
finally: 
    print('Até mais!')

# Isto é, ao invés de aparecer a mensagem de erro gigantesca, consigo especificar qual erro (exceção) está ocorrendo. 