# coding:utf-8
import xlrd
import xlwt

def read(data):
    Mysheet = data.sheets()[0]
    nrows = Mysheet.nrows
    ncols = Mysheet.ncols
    list = []
    # 逐行读取
    for i in range(nrows):
        list.append(Mysheet.row_values(i))
    return list, nrows, ncols

def compare(Sheet, list1, list2, ncol1, ncol2, nrow3):
    list1 = list1[2:]
    list2 = list2[2:]
    # 将相同的数据存入same
    same = []
    for i in list1:
        if i in list2:
            same.append(i)

    # 将list1与same不同的数据存入different1，list2与same不同的存入different2
    different1 = []
    different2 = []
    for i in list1:
        if i not in same:
            different1.append(i)
    for i in list2:
        if i not in same:
            different2.append(i)

    # 将same、different1、different2写入Final Result中
    for i in range(2, len(same) + 2):
        for j in range(ncol1):
            Sheet.write(i, j, same[i - 2][j])
        Sheet.write(i, ncol1, 'TRUE')
        for k in range(ncol1 + 1, ncol2 + 4):
            Sheet.write(i, k, same[i - 2][k - 4])

    for i in range(len(same) + 2, nrow3 - 4 - len(same)):
        for j in range(ncol1):
            Sheet.write(i, j, different1[i - 2 - len(same)][j])
        Sheet.write(i, ncol1, 'FALSE')

    for i in range(nrow3 - 4 - len(same), nrow3 - 4 - len(same) + len(different2)):
        for k in range(ncol1 + 1, ncol2 + 4):
            Sheet.write(i, k, different2[i - (nrow3 - 4 - len(same))][k - 4])
        Sheet.write(i, ncol1, "FALSE")

def set_style(name, height, bold=False):
    style = xlwt.XFStyle()  # 初始化样式

    font = xlwt.Font()  # 为样式创建字体
    font.name = name  # 'Times New Roman'
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
    data1 = xlrd.open_workbook(r'C:\Users\Jhon117\Desktop\demo\笔试\lab\data1.xlsx')
    data2 = xlrd.open_workbook(r'C:\Users\Jhon117\Desktop\demo\笔试\lab\data2.xlsx')
    list1, nrow1, ncol1 = read(data1)
    list2, nrow2, ncol2 = read(data2)
    nrow3 = nrow1 + nrow2
    ncol3 = ncol1 + ncol2
    Result = xlwt.Workbook(encoding='utf-8')
    Sheet1 = Result.add_sheet('Final Result', cell_overwrite_ok=True)
    # 表头
    for k in range(ncol3):
        Sheet1.write(0, k, '')
    #合并单元格
    Sheet1.write_merge(0, 0, 0, ncol3, 'Final Result', set_style('Times New Roman', 220, True))
    # 列名
    for i in range(ncol1):
        Sheet1.write(1, i, list1[1][i], set_style('Times New Roman', 220, True))
    Sheet1.write(1, ncol1, 'Result', set_style('Times New Roman', 220, True))
    for j in range(ncol1 + 1, ncol2 + 4):
        Sheet1.write(1, j, list2[1][j - 4], set_style('Times New Roman', 220, True))

    compare(Sheet1, list1, list2, ncol1, ncol2, nrow3)
    Result.save(r'C:\Users\Jhon117\Desktop\demo\笔试\lab\Result.xls')

if __name__ == '__main__':
    main()