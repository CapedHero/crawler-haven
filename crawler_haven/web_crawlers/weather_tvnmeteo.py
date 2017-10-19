import simplejson

import requests
from bs4 import BeautifulSoup

url = 'https://tvnmeteo.tvn24.pl/pogoda/warszawa,46800/na-dzis-na-jutro,1.html'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 ('
                         'KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
r = requests.get(url, headers=headers)

soup = BeautifulSoup(r.text, 'html.parser')
day_box, night_box = soup.find_all('div', class_='weatherBox rd7')
day_box_elements = list(day_box.descendants)
night_box_elements = list(night_box.descendants)

weather_overall = day_box_elements[13].lower()
weather_max = day_box_elements[22]
weather_min = night_box_elements[22]
weather_rain = day_box_elements[56]

print(simplejson.dumps({
    'weather_overall': weather_overall,
    'weather_max': weather_max,
    'weather_min': weather_min,
    'weather_rain': weather_rain,
}))
