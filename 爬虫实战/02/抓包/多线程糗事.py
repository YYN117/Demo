import urllib.request,urllib.error,re,threading
hearders = ('User-Agent','Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11')
opener = urllib.request.build_opener()
opener.addheaders = [hearders]
urllib.request.install_opener(opener)

class one(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        for i in range(1,10,2):
            # if i%2 != 0:
            #     i = i
            url = 'https://www.qiushibaike.com/8hr/page/' + str(i) + '/'
            pagedata = urllib.request.urlopen(url).read().decode('utf-8', 'ignore')
            pat = '<div class="content">.*?<span>(.*?)</span>.*?</div>'
            # pat = '<div class="content">(.*?)</div>'
            datalist = re.compile(pat, re.S).findall(pagedata)
            for j in range(len(datalist)):
                print('第{}页的第{}个段子的内容是：'.format(i, j + 1))
                print(datalist[j])

class two(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        for i in range(2,11,2):
            # if i%2 != 0:
            #     i = i
            url = 'https://www.qiushibaike.com/8hr/page/' + str(i) + '/'
            pagedata = urllib.request.urlopen(url).read().decode('utf-8', 'ignore')
            pat = '<div class="content">.*?<span>(.*?)</span>.*?</div>'
            # pat = '<div class="content">(.*?)</div>'
            datalist = re.compile(pat, re.S).findall(pagedata)
            for j in range(len(datalist)):
                print('第{}页的第{}个段子的内容是：'.format(i, j + 1))
                print(datalist[j])

t1 = one()
t2 = two()
t1.start()
t1.join()
t2.start()

