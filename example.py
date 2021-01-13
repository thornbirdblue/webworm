#!/usr/bin/python
import requests
url = 'http://www.baidu.com'
html = requests.get(url).content.decode()
print(html)
