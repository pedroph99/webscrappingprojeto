import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
path='C:/Users/pedro/Downloads/chromedriver_win32/chromedriver'

driver=webdriver.Chrome(path)

driver2=driver.get('https://redesim.jucepe.pe.gov.br/requerimentouniversal/NovoLogin.aspx')
digita_cpf=driver.find_element(by=By.ID, value='_ctl0_MainContent_txtCPFCNPJ')
digita_cpf.send_keys('247.256.174-15')
digita_senha=driver.find_element(by=By.ID, value='_ctl0_MainContent_txtSenha')
digita_senha.send_keys('Data.2019')

entra_site=driver.find_element(by=By.NAME, value='_ctl0:MainContent:btnEntrar')
entra_site.click()


