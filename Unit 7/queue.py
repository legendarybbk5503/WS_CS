class Queue:

    def __init__(self, queue: list, maxSize: int = None):
        if not isinstance(queue, list) or (not isinstance(maxSize, int) and maxSize is not None):
            raise TypeError
        
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

    def enqueue(self, item): #add item at [-1]
        if self.__isFull():
            raise Exception("The queue is full")
        else:
            self.__queue.append(item)

    def dequeue(self): #remove item at [0]
        if self.__isEmpty():
            raise Exception("The queue is empty")
        else:
            self.__queue.pop(0)
    
    def getQueue(self):
        return self.__queue

def main():
    s = Queue([1, 2, 3, 4, 5]) #dynamic
    s.enqueue(6)
    print(s.getQueue())
    s.dequeue()
    print(s.getQueue())

    q = Queue([1, 2, 3, 4, 5], 5) #static
    q.enqueue(6)
    print(q.getQueue())
    q.dequeue()
    print(q.getQueue())

if __name__ == "__main__":
    main()