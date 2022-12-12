from random import randint
from time import perf_counter_ns

class Sort():
    def __init__(self, __list):
        self.__list = __list

    def insertionSort(self):
        for i in range(1, len(self.__list)):
            now, pos = self.__list[i], i
            while pos > 0 and self.__list[pos-1] > now:
                self.__list[pos] = self.__list[pos-1]
                pos -= 1
            self.__list[pos] = now
        return self.__list

    def bubbleSort(self):
        for _ in range(len(self.__list)-1):
            for j in range(len(self.__list)-1):
                if self.__list[j] > self.__list[j+1]:
                    self.__list[j], self.__list[j+1] = self.__list[j+1], self.__list[j]
        return self.__list

    def mergeSort(self, _list = None):
        if _list is None: _list = self.__list
        if len(_list) > 1:
            mid = len(_list) // 2
            lefthalf = _list[:mid]
            righthalf = _list[mid:]

            self.mergeSort(lefthalf)
            self.mergeSort(righthalf)

            i, j, k = 0, 0, 0
            while i < len(lefthalf) and j < len(righthalf):
                if lefthalf[i] < righthalf[j]:
                    _list[k] = lefthalf[i]
                    i += 1
                else:
                    _list[k] = righthalf[j]
                    j += 1
                k += 1

            while i < len(lefthalf):
                _list[k] = lefthalf[i]
                i += 1
                k += 1
            
            while j < len(righthalf):
                _list[k] = righthalf[j]
                j += 1
                k += 1

        self.__list = _list
        return self.__list

    def binarySearch(self, x):
        _list, i, j = self.__list, 0, len(self.__list)-1
        while True:
            if _list[(i+j)//2] == x: return (i+j)//2
            elif i == j: return -1
            elif _list[(i+j)//2] > x: j = (i+j)//2-1
            elif _list[(i+j)//2] < x: i = (i+j)//2+1

    def linearSearch(self, x):
        i = [i for i in range(len(self.__list)) if self.__list[i] == x]
        return -1 if not len(i) else i[0]

def timeCounter(method):
    start = perf_counter_ns()
    method()
    stop = perf_counter_ns()
    return stop-start
    

def main(x):
    _list = [randint(1, 1000) for _ in range(x)]
    c = Sort(_list)
    print(timeCounter(c.insertionSort))
    print(timeCounter(c.bubbleSort))
    print(timeCounter(c.mergeSort))
    print(timeCounter(_list.sort))
    #print(timeCounter(c.binarySearch(66)))
    #print(timeCounter(c.linearSearch(67)))

if __name__ == "__main__":
    main(1000)
    main(2000)
