from bs4 import BeautifulSoup
import requests
url='https://redesim.jucepe.pe.gov.br/requerimentouniversal/NovoLogin.aspx'
login='https://redesim.jucepe.pe.gov.br/requerimentouniversal/NovoLogin.aspx'
request_data={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36 OPR/88.0.4412.53',

'origin': 'https://redesim.jucepe.pe.gov.br',  'referer': 'https://redesim.jucepe.pe.gov.br/requerimentouniversal/NovoLogin.aspx', 'content-type': 'text/html; charset=utf-8',
'_ctl0:MainContent:txtCPFCNPJ': '247.256.174-15', '_ctl0:MainContent:txtSenha': 'Data.2019', '_ctl0MainContent:btnEntrar': 'Entrar' }


requisicao1= requests.session()

get1=requisicao1.get(url)
print(requests.__version__)
post1=requisicao1.post(login, headers=request_data, data= request_data)

print(post1.status_code)
html1=BeautifulSoup(post1.text, 'html.parser')

print(html1.find('h3'))