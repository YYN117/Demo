# coding:utf-8
import xlrd
import xlwt
from xlutils.copy import copy
'''
不借助第三方库实现
目前问题有：
1.排序还未处理好
2.时间格式问题，data1和data2中的时间导入后变成了一个浮点型
'''

def read(data):
    # data1 = xlrd.open_workbook(r'C:\Users\Jhon117\Desktop\demo\笔试\data1.xlsx')
    Mysheet = data.sheets()[0]
    nrows = Mysheet.nrows
    ncols = Mysheet.ncols
    list = []
    for i in range(1,nrows):
        for j in range(ncols):
            list.append(Mysheet.cell(i,j).value)
    return list,nrows,ncols

def compare(Sheet,list1,list2,ncol1,ncol2,nrow3):
    #按行分组
    list1 = list1[3:]
    a = []
    for i in range(0,len(list1),3):
        a.append(list1[i:i+3])

    list2 = list2[3:]
    b = []
    for i in range(0,len(list2),3):
        b.append(list2[i:i+3])
    same = []
    for d1 in range(len(a)):
        for d2 in range(len(b)):
            # print(a[d1],b[d2])
            if a[d1] == b[d2]:
                same.append(a[d1])
    for i in range(2,len(same)+2):
        for j in range(ncol1):
            Sheet.write(i,j,same[i-2][j])
        Sheet.write(i,ncol1,'TRUE')
        for k in range(ncol1+1,ncol2+4):
            Sheet.write(i,k,same[i-2][k-4])

    #二维数组去重
    left = get_unique(a,same)[-(len(a)-len(same)):]
    right = get_unique(b,same)[-(len(b)-len(same)):]

    for i in range(2+len(same),nrow3-4-len(same)):
        for j in range(ncol1):
            Sheet.write(i,j,left[i-4][j])
        Sheet.write(i,ncol1,'FALSE')
    for i in range(nrow3-4-len(same), nrow3-4-len(same)+len(right)):
        for k in range(ncol1+1,ncol2+4):
            Sheet.write(i,k,right[i-(nrow3-4-len(same))][k-4])
        Sheet.write(i,ncol1,"FALSE")

def get_unique(tag,key):
    unique = []
    for j in range(len(key)):
        for i in range(len(tag)):
            if tag[i] != key[j]:
                unique.append(tag[i])
    return unique

def set_style(name,height,bold=False):
    style = xlwt.XFStyle()  # 初始化样式

    font = xlwt.Font()  # 为样式创建字体
    font.name = name # 'Times New Roman'
    font.bold = bold
    font.color_index = 4
    font.height = height

    # borders= xlwt.Borders()
    # borders.left= 6
    # borders.right= 6
    # borders.top= 6
    # borders.bottom= 6

    alignment = xlwt.Alignment()  # 创建对齐方式
    alignment.vert = xlwt.Alignment.VERT_CENTER  # 设置垂直对齐方式

    style.font = font
    # style.borders = borders看，

    return style

def main():
    data1 = xlrd.open_workbook(r'C:\Users\Jhon117\Desktop\demo\笔试\data1.xlsx')
    data2 = xlrd.open_workbook(r'C:\Users\Jhon117\Desktop\demo\笔试\data2.xlsx')
    list1,nrow1,ncol1 = read(data1)
    list2,nrow2,ncol2 = read(data2)
    nrow3 = nrow1 + nrow2
    ncol3 = ncol1 + ncol2
    Result = xlwt.Workbook(encoding='utf-8')
    Sheet1 = Result.add_sheet('Final Result', cell_overwrite_ok=True)
    #表头
    for k in range(ncol3):
        Sheet1.write(0,k,'')
    Sheet1.write_merge(0,0,0,ncol3,'Final Result',set_style('Times New Roman',220,True))
    #列名
    for i in range(ncol1):
        Sheet1.write(1,i,list1[i],set_style('Times New Roman',220,True))
    Sheet1.write(1,ncol1,'Result',set_style('Times New Roman',220,True))
    for j in range(ncol1+1,ncol2+4):
        Sheet1.write(1,j,list2[j-4],set_style('Times New Roman',220,True))

    compare(Sheet1,list1,list2,ncol1,ncol2,nrow3)

    Result.save(r'C:\Users\Jhon117\Desktop\demo\笔试\Result.xls')

main()
