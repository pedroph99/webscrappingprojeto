import requests

from bs4 import BeautifulSoup


response1=requests.get('https://www.habbo.com.br')

soupe=BeautifulSoup(response1.text, 'html.parser')

print(soupe.find_all('div'))