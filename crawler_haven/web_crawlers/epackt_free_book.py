#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests

url = 'https://www.packtpub.com//packt/offers/free-learning'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 ('
                         'KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
r = requests.get(url, headers=headers)

print(r.text[:200])
