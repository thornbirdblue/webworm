#!/usr/bin/python
import requests
url = 'https://www.baidu.com/s?tn=news&rtt=1&bsst=1&cl=2&wd=阿里巴巴'
html = requests.get(url).content.decode()
print(html)
