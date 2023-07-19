import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from pathlib import Path, os
from dotenv import load_dotenv

class SeleniumHelper:
    def __init__(self):
        self.driver = None

    def initialize_driver(self):
        profile_path = r'C:\Users\pedro\AppData\Local\Google\Chrome\User Data'
        options = Options()
        options.add_argument('window-size=1240,980')
        options.add_argument('--user-data-dir=' + profile_path)
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.get('https://gestordepedidos.ifood.com.br/#/home/pos/new-order/customer?utm_source=menu-lateral&utm_campaign=menulateral')

    def abrir_entrega_facil(self):
        self.driver = self.initialize_driver()

        if self.driver is None:
            print('driver é None')
        cont = 0
        while True:
            sleep(1)
            try:
                self.driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[1]/div[1]/div[3]/aside/nav/a[4]/div').click()
                break
            except:
                cont += 1
                if cont > 30:
                    print('Botão para clique não encontrado')
                    break       

    # def open_page(self,page):
    #     self.driver = self.initialize_driver()
    #     self.driver.get(page)
    #     self.driver.find_element(By.NAME, 'link-ifood').click()

#input('Digite ENTER para fechar...')
#navegador.close()