import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from pathlib import Path, os
from dotenv import load_dotenv
from time import sleep

def pedido_info(auth, num_pedido):
    headers = {
    'authority': 'api.saipos.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
    'authorization': f'{auth}',
    'origin': 'https://conta.saipos.com',
    'referer': 'https://conta.saipos.com/',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36',
    }

    response = requests.get(
        f'https://api.saipos.com/v1/stores/15618/sales/{num_pedido}?filter=%7B%22options%22:%7B%22getDeletedItems%22:true%7D%7D',
        headers=headers,
    )

    resposta = response.json()

    nome = resposta['customer']['full_name']
    telefone = resposta['customer']['phones'][0]['phone']
    rua = resposta['sale_delivery']['address']
    bairro = resposta['sale_delivery']['desc_district']
    cidade = resposta['sale_delivery']['store_district']['district']['city']['desc_city']
    numero_casa = resposta['sale_delivery']['address_number']
    complemento = resposta['sale_delivery']['address_complement']
    referencia = resposta['sale_delivery']['address_reference']
    total_produtos = resposta['total_amount_items']
    frete = resposta['sale_delivery']['store_district']['delivery_fee']
    valor_total = resposta['total_amount']
    forma_pagamento = resposta['payment_types'][0]['payment_type']['desc_store_payment_type']
    data = resposta['created_at']

    dict_pedido = {
        'numero_pedido': num_pedido,
        'nome_cliente': nome,
        'telefone': telefone,
        'data': f'{data[8:10]}-{data[5:7]}-{data[:4]}',
        'endereco_entrega': f'{rua}, {bairro}, {cidade}',
        'numero_entrega': numero_casa,
        'complemento': complemento,
        'referencia': referencia,
        'valor_produtos': float(total_produtos),
        'frete': float(frete),
        'total_pedido': float(valor_total),
        'forma_pagamento': forma_pagamento
    }

    return dict_pedido

def auth_saipos(navegador):
    navegador.find_element(By.NAME, 'link-saipos').click()
    user = str(os.getenv('user_saipos'))
    password = str(os.getenv('password_saipos'))
    aba_saipos = navegador.window_handles[1]
    navegador.switch_to.window(aba_saipos)
    # Fazer Login
    cont = 0
    while True:
        try:
            sleep(1)
            navegador.find_element(By.XPATH, '//*[@id="l-login"]/form/div[1]/div/input').send_keys(user)
            navegador.find_element(By.XPATH, '//*[@id="l-login"]/form/div[2]/div/input').send_keys(password)
            navegador.find_element(By.XPATH, '//*[@id="l-login"]/form/button/i').click()
            break
        except:
            cont += 1
            if cont > 60:             
                break
    # Derrubar outra seção com o usuário
    cont = 0
    while True:
        try:
            sleep(2)
            navegador.find_element(By.XPATH, '/html/body/div[2]/div[2]/p[2]/button[2]').click()
            print('passei aqui')
            break
        except:
            cont += 1 
            print('passei aqui no except')
            if cont > 60:             
                break

def abrir_entregaFacil(navegador):
    aba_ifood = navegador.window_handles[-1]
    navegador.switch_to.window(aba_ifood)

#g = requests.get('https://google.com')
#response = requests.get('https://conta.saipos.com/')
#if response != g:
#    pedido_info()
#else:
#    auth = auth_saipos()