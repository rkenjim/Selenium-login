#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Bibliotecas
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
import time
from getpass import getpass

#A qui definimos qual extenção/Browser que vamos usar, o de baixo no caso é o Chrome,
#Se for usar o Firefox no lugar de .Chrome() substitui por .geckodriver()

driver = webdriver.Chrome() 
driver.get("Aqui coloca o site que desenha fazer login")
time.sleep(5)

#para maximizar a tela, mas sinceramente não é 100% necessário pode tirar isso se quiser

driver.maximize_window()

#Preencher o campo email

driver.find_element(By.XPATH,'Coloque o caminho XPATH do campo para inserir o email').send_keys('Coloque o emai aqui')

# Clicar no botão Próxima tela, caso tenha outra tela para digitar a senha como no caso do Gmail por exemplo
#Caso o login e senha seja na mesma tela ignora essa parte

bot_log = driver.find_element(By.XPATH,'Xpath do Botão')

#Aqui poderia substituir por  bot_log.click(), deixei dessa maneira pois as vezes dá uma buggada
driver.execute_script("arguments[0].click();", bot_log)

time.sleep(5)

#Preencher o campo senha

sen = driver.find_element(By.XPATH,"Coloque o caminho do campo Xpath da senha")
sen.send_keys('Coloque a senha aqui')

#Clicar no botão Próximo

bot_senh = driver.find_element(By.XPATH,'Caminho Xpath do Botão')
driver.execute_script("arguments[0].click();", bot_senh)



# In[ ]:




