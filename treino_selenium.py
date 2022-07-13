# import selenium

import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from Analisacnpj import analisa
from treino import cria_workbook
#lista_cnpj é realizada pela função analisa, a qual retorna uma lista de cnpjs.







        




def roda_jucepe(_cnpj=None):

    path = '/home/pedromello/Downloads/chromedriver_linux64/chromedriver'

    driver = webdriver.Chrome(path)

    driver2 = driver.get('https://redesim.jucepe.pe.gov.br/requerimentouniversal/NovoLogin.aspx')
    digita_cpf = driver.find_element(by=By.ID, value='_ctl0_MainContent_txtCPFCNPJ')
    digita_cpf.send_keys('cpf')
    digita_senha = driver.find_element(by=By.ID, value='_ctl0_MainContent_txtSenha')
    digita_senha.send_keys('senha.2019')

    entra_site = driver.find_element(by=By.NAME, value='_ctl0:MainContent:btnEntrar')
    entra_site.click()

    driver.get('https://redesim.jucepe.pe.gov.br/requerimentouniversal/NovoTiposCertidao.aspx')

    inteiro_teor = driver.find_element(by=By.ID, value='_ctl0_MainContent_btnCertInteiroTeor')
    inteiro_teor.click()

    time.sleep(1)
    # _ctl0_MainContent_ddlTipoPesquisa
    seleciona_cnpj=driver.find_element(by=By.NAME, value='_ctl0:MainContent:ddlTipoPesquisa')
    selecionar=Select(seleciona_cnpj)
    selecionar.select_by_value('1')

   

    digita_cnpj=driver.find_element(by=By.ID, value='_ctl0_MainContent_txtCNPJ')
    digita_cnpj.send_keys(_cnpj)

    submit_button=driver.find_element(by=By.ID, value="_ctl0_MainContent_btnBuscar")
    submit_button.click()


    # javascript:__doPostBack('_ctl0$MainContent$btnCertInteiroTeor','')

    # pegar tabela class "tabela2" pegar [2] TD
    time.sleep(2)
    catch_tbody=driver.find_element(by=By.ID, value= '_ctl0_MainContent_dlEmpresa__ctl1_LinkButton1')
    catch_tbody.click()

    catch_all_td=driver.find_elements(by=By.CLASS_NAME, value= 'tabela2')

    time.sleep(1)
    all_td=catch_all_td[1].find_elements(by=By.TAG_NAME, value='td')

    return all_td[2].text
    # print(f'Achei: {all_td[2].text}')
    # for x in all_td:
    #     try:
    #         print(x.text[1])

    #     except:
    #         pass


guarda_dicionario=[]

def cria_dicionario(dicionario, cnpj, situacao):
    new_dict={ cnpj: situacao}
    dicionario.append(new_dict)

def roda_tudo(arquivo):
    a=analisa(arquivo)
    for x in range(len(a)):
        try:
            cria_dicionario(guarda_dicionario, a[x], roda_jucepe(a[x]))
            print(guarda_dicionario)
            time.sleep(5)
        except:
            print('%s é inválido e não pode ser lido pela JUCEPE' %(a[x]))
            cria_dicionario(guarda_dicionario, a[x], 'nao passou')
            time.sleep(5)
        
inicio=time.time()
roda_tudo('CNPJJ')
fim=time.time()
print(fim-inicio)
"""""
lista2=[]
for x in range(len(analisa('CNPJJ'))):
    lista2.append(guarda_dicionario[x][0])
print(lista2)
cria_workbook('moedas.xlsx', analisa('CNPJJ'), lista2 )
"""
lista2={}
for x in range(len(analisa('CNPJJ'))):
    lista2[x] = guarda_dicionario[x][analisa('CNPJJ')[x]]
print(lista2)
cria_workbook('jucepe.xlsx', analisa('CNPJJ'), lista2 )