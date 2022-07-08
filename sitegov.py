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




d=session.get('https://www.investing.com/portfolio/')

htmlmoeda=BeautifulSoup(d.content, 'html.parser')

print(htmlmoeda.find('h1'))

#r=session.ost(url+login, headers=request_data, data=data_info, cookies=b)
#print(r.text)

 