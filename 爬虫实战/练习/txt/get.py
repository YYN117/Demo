# -*- coding:UTF-8 -*-
import requests
from bs4 import BeautifulSoup
if __name__ == '__main__':
    target = 'https://www.biquku.co/106704/5438412.html'
    req = requests.get(url = target)
    html = req.text
    bf = BeautifulSoup(html)
    texts = bf.find_all('div',id="content")
    print(texts)
    print(texts[0].text.replace('\xa0'*4,'\n\n'))