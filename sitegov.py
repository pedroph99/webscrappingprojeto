from django import forms
import requests
from bs4 import BeautifulSoup
#logging in github


url='https://www.investing.com/members-admin/auth/signInByEmail/'
request_data={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36 OPR/88.0.4412.53',

'origin': 'https://www.investing.com',  'referer': 'https://www.investing.com'}

data_info = {'login': 'pedroph99@outlook.com',
        'password': 'ph454566'}

session=requests.session()


r=session.post(url, headers=request_data, data=data_info)

print(r.status_code)

