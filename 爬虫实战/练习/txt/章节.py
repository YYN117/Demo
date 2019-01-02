# -*- coding:UTF-8 -*-
import requests
from bs4 import BeautifulSoup
if __name__ == '__main__':
    target = 'https://www.biquku.co/106704/'
    server = 'https://www.biquku.co'
    req = requests.get(url=target)
    html = req.text
    div_bf = BeautifulSoup(html)
    div = div_bf.find_all('div',id='list')
    a_bf = BeautifulSoup(str(div[0]))
    a = a_bf.find_all('a')
    for i in a:
        print(i.string,server+i.get('href'))