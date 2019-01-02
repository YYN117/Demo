import os

def getAll(path,sp = ''):
    #得到当前目录下所有文件
    filesList = os.listdir(path)

    #处理每一个文件
    sp +='  '
    for fileName in filesList:
        #path/fileName 判断是否是路径
        fileAbsPath = os.path.join(path, fileName)
        if os.path.isdir(os.path.join(path,fileName)):
            print(sp + '目录：',fileName)
            #递归调用
            getAll(fileAbsPath,sp)
        else:
            print(sp + '普通文件:',fileName)
getAll(r'C:\Users\Jhon117\Desktop\demo\day7')