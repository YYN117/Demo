import csv

def readCsv(path):
    infoList = []
    with open(path,'r')as f:
        allFileInfo = csv.reader(f)
        print(allFileInfo)
        for row in allFileInfo:
            infoList.append(row)
    return infoList
path=r'C:\Users\Jhon117\Desktop\demo\day12\读写CSV\000001.csv'
readCsv(path)