import requests
from bs4 import BeautifulSoup

url = 'https://www.packtpub.com//packt/offers/free-learning'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 ('
                         'KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
r = requests.get(url, headers=headers)

soup = BeautifulSoup(r.text, 'html.parser')
free_book_div = soup.find('div', class_='dotd-title')

print(next(free_book_div.stripped_strings))
