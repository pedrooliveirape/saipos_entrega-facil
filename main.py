import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium_helper import SeleniumHelper
from time import sleep
from pathlib import Path, os
from dotenv import load_dotenv

options = Options()
options.add_argument('window-size=1240,980')
service = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=service, options=options)
navegador.get('http://127.0.0.1:8000/')


navegador.close()
