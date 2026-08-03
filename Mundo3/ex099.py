# FUNÇÃO QUE DESCOBRE O MAIOR # 

def maior(*num): 
    m = 0
    print('-'*40)
    print('Analisando valores...')
    for p, v in enumerate(num): 
        print(v, end=' ')
    
        if p == 0: 
            m = v 

        else: 
            if v > m: 
                m = v   
    print()
    print(f'Ao todo foram {len(num)} valores e o maior entre eles é o {m}') 

maior(2, 9, 4, 5, 7, 1) 
maior(5) 
maior() 
maior(-5, -3, -1)  