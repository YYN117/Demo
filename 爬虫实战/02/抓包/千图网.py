'''
http://www.58pic.com/piccate/3-0-0.html
http://www.58pic.com/piccate/3-0-0-default-0_2_0_0_default_0-2.html
http://www.58pic.com/piccate/3-0-0-default-0_2_0_0_default_0-3.html
http://www.58pic.com/haibaomoban/0/id-2.html

http://pic.qiantucdn.com/58pic/32/41/93/92058PIC2iZ0x0C2TcJ49_PIC2018.jpg!qtwebp324
http://pic.qiantucdn.com/58pic/32/41/93/92058PIC2iZ0x0C2TcJ49_PIC2018_1024.jpg
'''
import urllib.request,re,urllib.error
for i in range(1,10):
    pageurl = 'http://www.58pic.com/piccate/3-0-0-default-0_2_0_0_default_0-'+str(i)+'.html'
    data = urllib.request.urlopen(pageurl).read().decode('utf-8','ignore')
    pat = 'class="thumb-box" target="_blank".*?src="(.*?).jpg!'
    imglist = re.compile(pat).findall(data)
    for j in range(0,len(imglist)):
        try:
            thisimg = imglist[j]
            imgurl = thisimg
            file = 'C:/Users/Jhon117/Desktop/demo/22/'+str(i)+str(j)+'.jpg'
            urllib.request.urlretrieve(imgurl,filename=file)
            print('第{}页的第{}个图片'.format(i,j+1))
        except urllib.error.URLError as e:
            if hasattr(e,'code'):
                print(e.code)
            if hasattr(e,'reason'):
                print(e.reason)
        except Exception as e:
            print(e)
