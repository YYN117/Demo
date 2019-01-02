# coding:utf-8
import xlrd
import xlwt

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

def sort(Mysheet,nrows,ncols):
    # data1 = xlrd.open_workbook(r'C:\Users\Jhon117\Desktop\demo\笔试\Result.xls')
    Slist = []
    for i in range(2,nrows):
        Slist.append(Mysheet.row_values(i))

    Slist.sort(key = lambda l:(l[0],l[1],l[2]))
    for i in range(2,len(Slist)):
        for j in range(len(Slist[0])):
            Mysheet.write(i,j,Slist[i][j])
    return list,nrows,ncols

def main():
    data = xlrd.open_workbook(r'C:\Users\Jhon117\Desktop\demo\笔试\Result.xls')
    list1,nrow1,ncol1 = read(data)
    Result = xlwt.Workbook(encoding='utf-8')
    Sheet1 = Result.add_sheet('Final Result', cell_overwrite_ok=True)
    sort(Sheet1,nrow1,ncol1)

main()
