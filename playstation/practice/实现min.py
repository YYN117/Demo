def indexOfMin():
    lyst = eval(input())
    minIndex = 0
    currentIndex = 1
    while currentIndex < len(lyst):
        if lyst[minIndex] > lyst[currentIndex]:
            minIndex = currentIndex
        currentIndex += 1
    print(minIndex)
    print(lyst[minIndex])
if __name__ == '__main__':
    indexOfMin()