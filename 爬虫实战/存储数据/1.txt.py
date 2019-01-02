# coding:utf-8
#知乎热搜
import requests
from pyquery import PyQuery as pq

url = 'https://www.zhihu.com/explore'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
html = requests.get(url,headers=headers).text
doc = pq(html)
items = doc('.explore-tab .feed-item').items()
for item in items:
    question =  item.find('h2').text()
    # author = item.find('.author-link-line').text()
    author = item('.zm-item-rich-text.expandable.js-collapse-body')
    author = author.attr('data-author-name')
    ans = pq(item.find('.content').html()).text()
    # ans = item.find('.content').text()
    # file = open('explore.txt','a',encoding='utf-8')
    # file.write('\n'.join([question,author,ans]))
    # file.write('\n'+'='*50+'\n')
    # file.close()
    with open('explore.txt','a',encoding='utf-8') as f:
        f.write('\n'.join([question,author,ans]))
        f.write('\n'+'='*50+'\n')
