from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

navegador = webdriver.Chrome()

navegador.get("https://www.youtube.com/")

bnt_login = navegador.find_element(By.CSS_SELECTOR,'[aria-label="Fazer login"]')
bnt_login.click()

import time

time.sleep(10)