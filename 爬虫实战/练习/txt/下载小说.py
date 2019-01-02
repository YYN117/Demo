# -*- coding:UTF-8 -*-
import requests,sys
from bs4 import BeautifulSoup

class downloader(object):

    def __init__(self):
        self.target = 'https://www.biquku.co/106704/'
        self.server = 'https://www.biquku.co'
        self.names = [] #存放章节名
        self.urls = []  #存放章节连接
        self.nums = 0   #章节数

    def get_download_url(self):
        req = requests.get(url=self.target)
        html = req.text
        div_bf = BeautifulSoup(html)
        div = div_bf.find_all('div', id='list')
        a_bf = BeautifulSoup(str(div[0]))
        a = a_bf.find_all('a')

        self.nums = len(a[15:])
        for each in a[15:]:
            self.names.append(each.string)
            self.urls.append(self.server+each.get('href'))

    def get_contents(self,target):
        req = requests.get(url=target)
        html = req.text
        bf = BeautifulSoup(html)
        texts = bf.find_all('div', id="content")
        ts = texts[0].text.replace('\xa0'*4, '\n\n')
        return ts

    def writer(self,name,path,text):
        write_flag = True
        with open(path,'a',encoding='utf-8') as f:
            f.write(name + '\n')
            f.writelines(text)
            f.write('\n\n')

if __name__ == '__main__':
    dl = downloader()
    dl.get_download_url()
    print('开始下载')

    for i in range(dl.nums):
        dl.writer(dl.names[i],'永恒.txt',dl.get_contents(dl.urls[i]))
        sys.stdout.write(' 已下载：%.3f%%'% float(i/dl.nums)+'\r')
        sys.stdout.flush()
    print('完成')