def bubbleSort(sortList):
    sorted = False
    length = len(sortList)
    while !sorted:
        for i in range(length - 2):
            if sortList[i] > sortList[i+1]:
                sortList[i] = sortList[i+1]
                sortList[i+1] = sortList[i]
                sorted = False
    return sortList