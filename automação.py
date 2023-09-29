import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

contatos_df = pd.read_excel('C:/Users/Usuário/Desktop/contatos.xlsx')
contatos_df.head()


import urllib

navegador = webdriver.Chrome()
navegador.get("https://web.whatsapp.com/")

while len(navegador.find_elements(By.ID,"side")) < 1:
    time.sleep(1)
    
for i, mensagem in enumerate(contatos_df['mensagem']):
    pessoa = contatos_df.loc[i,'nome']
    numero = contatos_df.loc[i,'numero']
    texto = urllib.parse.quote(f"Olá {pessoa},{mensagem}")
    link = f"https://web.whatsapp.com/send?phone={numero}&text={texto}"
    navegador.get(link)
    
    while len(navegador.find_elements(By.ID,"side")) < 1:
        time.sleep(5)
                               
    navegador.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div/p/span').send_keys(Keys.ENTER)   
    time.sleep(10)                           
    