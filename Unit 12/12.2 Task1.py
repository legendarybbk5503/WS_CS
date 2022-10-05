class Animal:
    def __init__(self, s, n):
        self.__state = s
        self.__size = n

    def feed(self):
        self.__size += 1
        print(f"{self.__state} fed")
    
    def getState(self):
        return self.__state
    
    def getSize(self):
        return self.__size

class Fish(Animal):
    def __init__(self, s):
        super().__init__(s, 1)
        self.__maxSize = 2
    
    def setMaxSize(self, m):
        self.__maxSize = m
    
    def feed(self):
        self.__size += 2
        print(f"{self.__state} fed")
        if self.__size >= self.__maxSize:
            self.__state = "BIG FISH"

class Duck(Animal):
    def __init__(self, s, n):
        super().__init__(s, n)
    
    def feed(self):
        super().feed()
        if self.__size == 5:
            self.__state = "BIG DUCK"

def main():
    thisFish = Fish("little fish")
    thisFish.setMaxSize(3)
    thisDuck = Duck("little duck", 1)
    for _ in range(3):
        thisDuck.feed()
        print(thisDuck.getState())
        thisFish.feed()
        print(thisFish.getState())

if __name__ == "__main__":
    main()