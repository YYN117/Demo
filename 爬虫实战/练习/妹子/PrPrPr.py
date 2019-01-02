import requests,os,time,threading
from bs4 import  BeautifulSoup

def download_page(url):
    '''
    下载界面,利用Requests
    '''

    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'}
    r = requests.get(url,headers=headers)
    r.encoding = 'gb2312'
    return r.text

def get_pic_list(html):
    '''
    获取页面图片列表
    :param html:
    :return:
    '''
    soup = BeautifulSoup(html,'html.parser')
    pic_list = soup.find_all('li',class_='wp_item')
    for i in pic_list:
        a_tag = i.find('h3',class_='tit').find('a')
        link = a_tag.get('href')
        text = a_tag.get_text()
        get_pic(link,text)

def get_pic(link,text):
    html = download_page(link)
    soup = BeautifulSoup(html,'html.parser')
    pic_list = soup.find('div',id='picture').find_all('img')
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'}
    create_dir('pic/{}'.format(text))
    for i in pic_list:
        pic_list = i.get('src')
        r = requests.get(pic_link,headers = headers)
        with open('pic/{}/{}'.format(text,pic_link.split('/')[-1]),'wb') as f:
            f.write(r.content)
            time.sleep(1)

def create_dir(name):
    if not os.path.exists(name):
        os.mkdir(name)

def execute(url):
    page_html = download_page(url)
    get_pic_list(page_html)

def main():
    create_dir('pic')
    queue = [i for i in range(1,72)]
    threads = []
    while len(queue)>0:
        for thread in threads:
            if not thread.is_alive():
                threads.remove(thread)
        while len(threads) < 5 and len(queue) > 0:  # 最大线程数设置为 5
            cur_page = queue.pop(0)
            url = 'http://meizitu.com/a/more_{}.html'.format(cur_page)
            thread = threading.Thread(target=execute, args=(url,))
            thread.setDaemon(True)
            thread.start()
            print('{}正在下载{}页'.format(threading.current_thread().name, cur_page))
            threads.append(thread)

if __name__ == '__main__':
    main()