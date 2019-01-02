import xlrd,xlwt,xlsxwriter
#设置要合并的所有文件
allxls = ['E:/1.xls','E:/2.xls']
#设置合并到的文件
endxls = 'E:/3.xlsx'

#打开表格
def open_xls(file):
    try:
        fh = xlrd.open_workbook(file)
        return fh
    except Exception as e:
        print('ERROR:'+e)

#获取sheet
def getsheet(fh):
    return fh.sheets()

#获取sheet行数
def getnrows(fh,sheet):
    table = fh.sheets()[sheet]
    content = table.nrows
    return content

#读取某个文件的内容并返回行的内容
def getfilect(fl,shnum):
    fh = open_xls(fl)
    table = fh.sheet_by_name(shname[shnum])
    num = getnrows(fh,shnum)
    lenvalue = len(rvalue)
    for row in range(0,num):
        rdata = table.row_values(row)
        rvalue.append(rdata)
    filevalue.append(rvalue[lenvalue:])
    return filevalue

#存储所有读取的结果
filevalue = []
#存储一个标签的结果
svalue = []
#存储一行结果
rvalue = []
#存储各sheet名
shname = []

#读取第一个待读文件，获得sheet数
fh = open_xls(allxls[0])
sh = getsheet(fh)
x = 0
for sheet in sh:
    shname.append(sheet.name)
    svalue.append([])
    x += 1
#依次读取各sheet的内容
#依次读取各文件当前sheet内容
for shnum in range(0,x):
    for fl in allxls:
        print('读取文件：'+str(fl)+'第'+str(shnum)+'个标签')
        filevalue = getfilect(fl,shnum)
    svalue[shnum].append(filevalue)
#由于append有叠加关系，分析可得所以信息均在svalue[0][0]中存储
#svalue[0][0]元素数量为sheet标签数（sn）*文件数（fn）
sn =x
fn = len(allxls)
endvalue = []

def getsvalue(k):
    for z in range(k,k+fn):
        endvalue.append(svalue[0][0][z])
    return endvalue

#打开最终写入的文件
wb1 = xlsxwriter.Workbook(endxls)
#创建一个sheet工作对象
ws = wb1.add_worksheet()
polit = 0
linenum = 0
#依次遍历每个sheet中的数据
for s in range(0,sn*fn,fn):
    thisvalue = getsvalue(s)
    tvalue = thisvalue[polit]
    #将一个标签内容写入新文件中
    for a in range(0,len(tvalue)):
        for b in range(0,len(tvalue[a])):
            for c in range(0,len(tvalue[a][b])):
                data = tvalue[a][b][c]
                ws.write(linenum,c,data)
            linenum += 1
    polit = len(thisvalue)
wb1.close()