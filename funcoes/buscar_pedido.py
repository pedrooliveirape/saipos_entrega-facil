import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from pathlib import Path, os
from dotenv import load_dotenv
from selenium_helper import SeleniumHelper
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

def auth_saipos():
    pass

def abrir_entregaFacil(form):
    print(form['pagamento_entrega'].value())
    profile_path = r'C:\Users\pedro\AppData\Local\Google\Chrome\User Data'
    options = Options()
    options.add_argument('window-size=1240,980')
    options.add_argument('--user-data-dir=' + profile_path)
    service = Service(ChromeDriverManager().install())
    navegador = webdriver.Chrome(service=service, options=options)
    navegador.get('https://gestordepedidos.ifood.com.br/#/home/orders/now')

    # Clicar no ENtrega Fácil
    cont = 0
    while True:
        sleep(1)
        try:
            navegador.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[1]/div[1]/div[3]/aside/nav/a[4]/div').click()
            break
        except:
            cont += 1
            if cont > 30:
                print('Botão para clique não encontrado')
                break
    # Digitar na barra de endereço do cliente
    cont = 0
    while True:
        sleep(1)
        try:
            navegador.find_element(By.XPATH, '//*[@id="downshift-3-input"]').send_keys(form['endereco_entrega'].value())            
            break
        except:
            cont += 1
            if cont > 30:
                print('input para digitar não encontrado')
                break

    # Preencher todas as informações
    # Número do endereço
    cont = 0
    while True:
        sleep(1)
        try:
            # Número do endereço para entrega
            navegador.find_element(By.XPATH, '//*[@id="streetNumber"]').send_keys(form['numero_entrega'].value())
            # Complemento
            if form['complemento'].value() is not None:
                navegador.find_element(By.XPATH, '//*[@id="complement"]').send_keys(form['complemento'].value())
            else: 
                navegador.find_element(By.XPATH, '//*[@id="withoutComplement"]').click()
            # Ponto de referência
            if form['referencia'].value() is not None:
                navegador.find_element(By.XPATH, '//*[@id="reference"]').send_keys(form['complemento'].value())
            else:
                navegador.find_element(By.XPATH, '//*[@id="reference"]').send_keys('.')
            # Nome do cliente
            navegador.find_element(By.XPATH, '//*[@id="name"]').send_keys(form['nome_cliente'].value())
            # Whatsapp do cliente
            navegador.find_element(By.XPATH, '//*[@id="telephone"]').send_keys(form['telefone'].value())
            # Valor do pedido
            navegador.find_element(By.XPATH, '//*[@id="orderPrice"]').send_keys(form['valor_produtos'].value())
            if not 'Pix' in form['forma_pagamento'].value():
                # Solicitar pagamento na entrega
                navegador.find_element(By.XPATH, '//*[@id="enabled"]').click()
                # Taxa de entrega
                navegador.find_element(By.XPATH, '//*[@id="deliveryPrice"]').send_keys(form['valor_produtos'].value())
                # Pedir Maquinhinha
                navegador.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[1]/div[1]/div[3]/div/div[2]/div/div/form/div/div[1]/div[3]/div/div[2]/label/div/div/input').click()
                # Escolher forma de pagamento
                if 'Crédito' in form['forma_pagamento'].value():
                    navegador.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[1]/div[1]/div[3]/div/div[2]/div/div/form/div/div[1]/div[3]/div/div[3]/label[1]/div/div[1]/input').click()
                    navegador.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[1]/div[1]/div[3]/div/div[2]/div/div/form/div/div[1]/div[3]/div/div[4]/div/label[3]/div/div/input').click()
                elif 'Débito' in form['forma_pagamento'].value():
                    navegador.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[1]/div[1]/div[3]/div/div[2]/div/div/form/div/div[1]/div[3]/div/div[3]/label[2]/div/div[1]/input').click()
                    navegador.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[1]/div[1]/div[3]/div/div[2]/div/div/form/div/div[1]/div[3]/div/div[4]/div/label[5]/div/div/input').click()   
            break
        except:
            cont += 1
            if cont > 60:
                print('input para digitar não encontrado')
                break
    
    while True:
        resp = input('Digite sair para fechar...')
        if resp == 's':
            break

    navegador.close()    