path = r'C:\Users\Jhon117\Desktop\demo\day7\file2.txt'
with open(path,'wb') as f1:
    str = 'yyn iuhafafaf'
    f1.write(str.encode('utf-8'))

with open(path, 'rb')as f2:
    data = f2.read()
    print(data)
    print(type(data))
    newData = data.decode('utf-8')
    print(type(newData))