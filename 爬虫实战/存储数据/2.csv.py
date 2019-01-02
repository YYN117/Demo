import csv

with open('data.csv','w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['id','name','age'])
    writer.writerow(['1001','Mike',20])
    writer.writerow(['1002', 'Niko', 35])
    writer.writerow(['1003', 'Raymond', 24])

with open('data1.csv','w') as csvfile:
    writer = csv.writer(csvfile,delimiter=' ')
    writer.writerow(['id','name','age'])
    writer.writerow(['1001','Mike',20])
    writer.writerow(['1002', 'Niko', 35])
    writer.writerow(['1003', 'Raymond', 24])

with open('data3.csv','w') as csvfile:
    fieldnames = ['id','name','age']
    writer = csv.DictWriter(csvfile,fieldnames = fieldnames)
    writer.writeheader()
    writer.writerow({'id':'1001','name':'Mike','age':20})
    writer.writerow({'id': '1002', 'name': 'Bob', 'age': 22})
    writer.writerow({'id': '1003', 'name': 'Jack', 'age': 46})

with open('data.csv','r',encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)