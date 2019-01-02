import requests,re,os,json
from urllib.parse import urlencode
from requests.exceptions import RequestException
from bs4 import BeautifulSoup
from hashlib import md5

def get_page(offset):
    params = {
        'offset':offset,
        'format':'json',
        'keyword':'街拍',
        'autoload':'true',
        'count':'20',
        'cur_tab':'1',
    }
    url = 'http://www.toutiao.com/search_content/?'+urlencode(params)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except requests.ConnectionError:
        print('请求出错')
        return None

def parse_page_index(html):
    data = json.loads(html)
    if data and 'data' in data.keys():
        for item in data.get('data'):
            yield item.get('article_url')

def get_page_detail(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('请求详情错误',url)
        return None

def parse_page_detail(html):
    soup = BeautifulSoup(html,'lxml')
    title = soup.select('title')[0].get_text()
    print(title)
    images_pattern = re.compile('var gallery = (.*?);',re.S)
    result = re.search(images_pattern,html)
    if result:
        print(result.group(1))


def main():
    html = get_page(0)
    for url in parse_page_index(html):
        # print(url)
        html = get_page_detail(url)
        if html:
            parse_page_index(html)

if __name__ == '__main__':
    main()