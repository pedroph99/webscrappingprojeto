from aiohttp import Payload
from django import forms
import requests
from bs4 import BeautifulSoup
#logging in github


url='https://br.investing.com'
login='/members-admin/auth/signInByEmail/'
request_data={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36 OPR/88.0.4412.53',

'origin': 'https://www.investing.com',  'referer': 'https://www.investing.com'}


session=requests.Session()
a=session.get(url)

b=a.cookies
print(b)
data_info = {'email': 'pedroph99@outlook.com',
        'password': 'ph454566',
                }


c=session.post(url+login, data=data_info)
print(c.text)
print(c.status_code)


d=session.get('https://www.investing.com/portfolio/')

htmlmoeda=BeautifulSoup(d.content, 'html.parser')

tbodypage=htmlmoeda.find('tbody', {'id': 'tbody_overview_34092673'})

parseador=tbodypage.find_all('tr')

for x in parseador:

        try:
                moeda=x.find('td', {'data-column-name':'name'})
                moeda2=moeda.find('span')
                print(moeda2.text)
        except:
                pass








#