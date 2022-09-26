class Sort():
    def __init__(self, __list):
        self.__list = __list

    def InsertionSort(self):
        for i in range(1, len(self.__list)):
            now, pos = self.__list[i], i
            while pos > 0 and self.__list[pos-1] > now:
                self.__list[pos] = self.__list[pos-1]
                pos -= 1
            self.__list[pos] = now
        return self.__list

    def BubbleSort(self):
        for _ in range(len(self.__list)-1):
            for j in range(len(self.__list)-1):
                if self.__list[j] > self.__list[j+1]:
                    self.__list[j], self.__list[j+1] = self.__list[j+1], self.__list[j]
        return self.__list

    def MergeSort(self, _list = None):
        if _list is None: _list = self.__list
        if len(_list) > 1:
            mid = len(_list) // 2
            lefthalf = _list[:mid]
            righthalf = _list[mid:]

            self.MergeSort(lefthalf)
            self.MergeSort(righthalf)

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

    def BinarySearch(self, x):
        _list, i, j = self.__list, 0, len(self.__list)-1
        while True:
            if _list[(i+j)//2] == x: return (i+j)//2
            elif i == j: return -1
            elif _list[(i+j)//2] > x: j = (i+j)//2-1
            elif _list[(i+j)//2] < x: i = (i+j)//2+1
    
    def LinearSearch(self, x):
        i = [i for i in range(len(self.__list)) if self.__list[i] == x]
        return -1 if not len(i) else i[0]

def main():
    _list = [15, 73, 29, 66, 35, 11, 43, 21]
    c = Sort(_list)
    print(c.InsertionSort())
    print(c.BubbleSort())
    print(c.MergeSort())
    print(c.BinarySearch(66))
    print(c.LinearSearch(67))

if __name__ == "__main__":
    main()
