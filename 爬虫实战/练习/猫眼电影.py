# coding:utf-8
import requests,re,json,time

def get_one_page(url):
    headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        return None

def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name">'
                         + '<a.*?>(.*?)</a>.*?"star">(.*?)</p>.*?releasetime">(.*?)</p>'
                         + '.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)
    items = re.findall(pattern,html)
    for item in items:
        yield {
            '排名':item[0],
            '海报':item[1],
            '片名':item[2].strip(),
            '主演':item[3].strip()[3:],
            '上映时间':item[4].strip()[5:],
            '评分':item[5].strip()+item[6].strip()
        }

def write_to_file(item):
    with open('maoyan.txt','a',encoding='utf-8') as f:
        f.write(json.dumps(item,ensure_ascii=False) + '\n')


def main(offset):
    url='https://maoyan.com/board/4?offset='+str(offset)
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)

if __name__ == '__main__':
    for i in range(0,100,10):
        main(i)
        # time.sleep(1)

