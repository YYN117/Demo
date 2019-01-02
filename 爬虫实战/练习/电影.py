import requests,json
from lxml import etree

#请求数据
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5514.400 QQBrowser/10.1.1660.400"}
url = 'https://movie.douban.com/cinema/nowplaying/nanjing/'
response = requests.get(url,headers = headers)
# print(response.text)    #打印源代码
text = response.text

#解析
parser = etree.HTML(text)

lis = parser.xpath('//li[@data-category="nowplaying"]') # /获取直接子节点，//获得子孙节点

movies = []
for li in lis:
    movie = {}
    img = li.xpath(".//img/@src")
    title = li.xpath("@data-title")[0]
    score = li.xpath("@data-score")[0]
    director = li.xpath("@data-director")[0]
    actors = li.xpath("@data-actors")[0]
    movie['tite'] = title
    movie['score'] = score
    movie['director'] = director
    movie['actors'] = actors
    movie['img'] = img
    movies.append(movie)

with open('movies.json','w',encoding='utf-8') as fp:
    json.dump(movies,fp,ensure_ascii=False) #ensure_ascii设置为False使得不显示utf-8
