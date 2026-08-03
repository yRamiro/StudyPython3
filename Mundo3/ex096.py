# FUNÇÃO QUE CALCULA ÁREA # 

def área(l, c):  
    print('-'*30)
    print("CÁLCULO DA ÁREA")
    print('-'*30)
    print(f'A área do terreno é de {l*c:.2f} m²') 



l = float(input('Digite a largura do terreno em metros: ')) 
c = float(input('Digite o comprimento do terro em metros: ')) 
área(l,c)