
from urllib import request
import chardet

if __name__ == '__main__':
    response = request.urlopen('http://fanyi.baidu.com/')
    html = response.read()
    charset = chardet.detect(html)
    print(chardet)
    html = html.decode('utf-8')
    print(html)