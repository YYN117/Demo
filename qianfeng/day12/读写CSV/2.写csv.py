import csv

def writeCsv(path,data):
    with open(path,'w') as f:
        writer = csv.writer(f)
        for rowData in data:
            writer.writerow(rowData)

path = r'C:\Users\Jhon117\Desktop\demo\day12\读写CSV\000002.csv'

writeCsv(path,[[1,2,3],[4,5,6],[7,8,9]])
