import random

def linearSearch(searchList, searchVal):
    count = 0
    for i in range(len(searchList)):
        count += 1
        if searchList[i] == searchVal:
            return i, count
    return "Value not found", count

def binarySearch(searchList, searchVal):
    start = 0
    end = len(searchList) - 1
    count = 0
    while start <= end:
        mid = (start + end) // 2
        count += 1
        if searchList[mid] == searchVal:
            return mid, count
        elif searchList[mid] < searchVal:
            start = mid + 1
        elif searchList[mid] > searchVal:
            end = mid - 1
    return "Value not found", count

def recursiveBinarySearch(searchList, searchVal, *args):
    if args:
        start, end = args[0], args[1]
    else:
        start, end = 0, len(searchList)
    
    mid = (start + end) // 2
    if searchList[mid] == searchVal:
        return mid
    elif start == end:
        return "Value not found"
    elif searchList[mid] < searchVal:
        return recursiveBinarySearch(searchList, searchVal, mid+1, end)
    elif searchList[mid] > searchVal:
        return recursiveBinarySearch(searchList, searchVal, start, mid-1)


def getVal():
    try: num = int(input("Type an integer: "))
    except Exception as e:
        print(e)
        return getVal()
    finally: return num

def generateList(num):
    _list = list(range(1, num+1))
    return _list


def test(n, tests):
    LCount = 0
    BCount = 0
    for _ in range(tests):
        searchList = generateList(n)
        searchVal = random.randint(1, tests)
        LCount += linearSearch(searchList, searchVal)[1]
        BCount += binarySearch(searchList, searchVal)[1]
    return round(LCount/tests, 3), round(BCount/tests, 3)




searchVal = getVal()
searchList = generateList(10)
print(linearSearch(searchList, searchVal))
print(recursiveBinarySearch(searchList, searchVal))
print(binarySearch(searchList, searchVal))

for i in [10, 100, 1000, 10_000, 100_000]:
    testResult = test(i, 1000)
    print(f"Average test for linear search: {testResult[0]}")
    print(f"Average test for binary search: {testResult[1]}")
    print(f"Difference of number of test needed: {round(testResult[0] - testResult[1], 3)}")
input()