musicLrc = """
"""
import time
lrcDict={}
musicLrcList = musicLrc.splitlines()
# print(musicLrcList)

for lrcLine in musicLrcList:
    lrcLineList = lrcLine.split(']')
    for index in range(len(lrcLineList)-1):
        timeStr = lrcLineList[index][1:]
        # print(timeStr)
        timeList = timeStr.split(':')
        time = float(timeList[0])*60+float(timeList[1])
        print(time)
        lrcDict[time] = lrcLineList[-1]

allTimeList = []
for key in lrcDict:
    allTimeList.append(key)
allTimeList.sort()
print(allTimeList)
while 1:
    getTime = float(input('>>>'))

    for n in range(len(allTimeList)):
        tempTime = allTimeList[n]
        if getTime < tempTime:
            break
    if n ==0:
        print('时间太小')
    else:
        print(lrcDict[allTimeList[n-1]])

while 1:
    getTime = 0
