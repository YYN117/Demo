'''
https://s.taobao.com/list?spm=a21bo.2017.201867-links-0.27.57fc11d9zJKOQY&q=T%E6%81%A4&cat=16&seller_type=taobao&oetag=6745&source=qiangdiao

https://s.taobao.com/list?spm=a21bo.2017.201867-links-0.27.57fc11d9zJKOQY&q=T%E6%81%A4&cat=16&seller_type=taobao&oetag=6745&source=qiangdiao&bcoffset=12&s=60

https://s.taobao.com/list?spm=a21bo.2017.201867-links-0.27.57fc11d9zJKOQY&q=T%E6%81%A4&cat=16&seller_type=taobao&oetag=6745&source=qiangdiao&bcoffset=12&s=120

https://s.taobao.com/search?q=搜索词&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306

https://s.taobao.com/search?q=搜索词&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&bcoffset=3&ntoffset=3&p4ppushleft=1%2C48&s=44

https://s.taobao.com/search?q=搜索词&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&bcoffset=0&ntoffset=6&p4ppushleft=1%2C48&s=88

https://g-search2.alicdn.com/img/bao/uploaded/i4/i3/2002005727/TB2k7b4kb5YBuNjSspoXXbeNFXa_!!2002005727-0-item_pic.jpg_360x360Q90.jpg_.webp

'''

import urllib.request,re
keyname = '热裤'
head = ('User-Agent','Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1')
opener = urllib.request.build_opener()
opener.addheaders = [head]
urllib.request.install_opener(opener)

#quote用于编码
key = urllib.request.quote(keyname)
for i in range(0,2):
    url = 'https://s.taobao.com/search?q='+key+'&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&bcoffset=0&ntoffset=6&p4ppushleft=1%2C48&s='+str(i*44)
    data = urllib.request.urlopen(url).read().decode('utf-8','ignore')
    pth = 'pic_url":"//(.*?)"'
    imageurl = re.compile(pth).findall(data)
    for j in range(0,len(imageurl)):
        thisimg  =  imageurl[j]


print(imageurl)


