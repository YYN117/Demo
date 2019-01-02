
import os
import collections
def getAllDirQU(path):
    queue = collections.deque()
    #进队
    queue.append(path)

    while len(queue) !=0:
        #出队
        dirPath = queue.popleft()
        #找出所以的文件
        firesList = os.listdir(dirPath)

        for fileMame in firesList:
            #绝对路径
            fileAbsPath = os.path.join(dirPath,fileMame)
            #判断是否是目录，是则进队，否则打印
            if os.path.isdir(fileAbsPath):
                print('目录：' + fileMame)
                queue.append(fileAbsPath)
            else:
                print('普通文件:'+ fileMame)

getAllDirQU(r'C:\Users\Jhon117\Desktop\demo\day7')