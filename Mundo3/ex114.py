# SITE ESTÁ ACESSÍVEL? # 
import requests 

try: 
    requests.get('https://pudim.com.br') 
except:
    print('\033[31mERRO! O site Pudim está inacessível no momento!\033[m') 
else: 
    print('O site Pudim está disponível!')