import pickle  #数据持久性模块

myList = [1,2,3,4,5,'sunk is a good man']
path = r'C:\Users\Jhon117\Desktop\demo\day7\file3.txt'
f = open(path,'wb')

pickle.dump(myList,f)

f.close()

#读取
f1 = open(path,'rb')
tempList = pickle.load(f1)
print(tempList)
f1.close()

