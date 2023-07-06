import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from funcoes.buscar_pedido import auth_saipos, pedido_info
from time import sleep
from pathlib import Path, os
from dotenv import load_dotenv

options = Options()
options.add_argument('window-size=1240,980')
#options.add_argument('--headless')
service = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=service, options=options)
navegador.get('http://127.0.0.1:8000/')
# auth_saipos(navegador)
teste = pedido_info(auth=str(os.getenv('auth_saipos')), num_pedido=187794989)
print(teste)
input('Digite ENTER para fechar...')
navegador.close()
