class Queue:

    def __init__(self, queue, maxSize = None):
        self.__queue = queue

        #maxSize = None => dynamic
        #maxSize = n    => static with maxSize n
        if maxSize is None:
            self.__mode = "dynamic"
        else:
            self.__mode = "static"
            self.__maxSize = maxSize

    def __isFull(self):
        if self.__mode == "dynamic": return False  #dynamic queue won't be full
        return len(self.__queue) == self.__maxSize 
    
    def __isEmpty(self):
        return len(self.__queue) == 0

    def add(self, item): #add item at [-1]
        if self.__isFull():
            raise Exception("The queue is full")
        else:
            self.__queue.append(item)

    def remove(self): #remove item at [0]
        if self.__isEmpty():
            raise Exception("The queue is empty")
        else:
            self.__queue.pop(0)
    
    def getQueue(self):
        return self.__queue

def main():
    s = Queue([1, 2, 3, 4, 5]) #dynamic
    s.add(6)
    print(s.getQueue())
    s.remove()
    print(s.getQueue())

    q = Queue([1, 2, 3, 4, 5], 5) #static
    q.add(6)
    print(q.getQueue())
    q.remove()
    print(q.getQueue())

if __name__ == "__main__":
    main()