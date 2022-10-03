class Animal():
    def __init__(self, state, size):
        self.__state__ = state
        self.__size__ = size

    def feed(self):
        self.__size__ += 1
        print("Fish fed")
        print(self.__size__)
        if self.__size__ == 5:
            self.__state__ = "FISH"
    
    def getState(self):
        return self.__state__
    
    def getSize(self):
        return self.__size__
        

thisFish = Animal("Fish", 1)
print(thisFish.getState())
print("is of size ", thisFish.getSize())

while thisFish.getState() != "FISH":
    thisFish.feed()
print("It is now a big")
print(thisFish.getState())
print(thisFish.getSize())