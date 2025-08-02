from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)

navegador = webdriver.Chrome(options=options)

navegador.get("https://www.youtube.com/")

bnt_login = navegador.find_element(By.CSS_SELECTOR,'[aria-label="Fazer login"]')
bnt_login.click()


email_input = WebDriverWait(navegador,10).until(
    EC.presence_of_element_located((By.ID,"identifierId"))
)

email_input.send_keys("seu email")

bnt_avanca_email = WebDriverWait(navegador,10).until(
    EC.element_to_be_clickable((By.XPATH,"//span[text()='Avançar']"))
)

bnt_avanca_email.click()

senha_input = WebDriverWait(navegador,15).until(
    EC.presence_of_element_located((By.NAME,"Passwd"))
)
senha_input.send_keys("sua senha do email")


bnt_avançar_senha = WebDriverWait(navegador,10).until(
    EC.element_to_be_clickable((By.XPATH,"//span[text()='Avançar']"))
)

bnt_avançar_senha.click()

import time


time.sleep(20)
