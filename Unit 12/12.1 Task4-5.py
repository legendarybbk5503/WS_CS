class Car():
    def __init__(self, reg, make):
        self.__reg__ = reg
        self.__make__ = make
        self.__milage__ = 0
        self.__doi__ = ""
    
    def getReg(self):
        return self.__reg__
    def getMake(self):
        return self.__make__
    def getMilage(self):
        return self.__milage__
    def getDoi(self):
        return self.__doi__
    
    def setInspection(self):
        self.__milage__ = input("Enter the mileage: ")
        self.__doi__ = input("Enter the date of inspection: ")
        print("updated")

def main():
    myCar = Car("ABC 123", "XXX")
    myCar.setInspection()
    print(myCar.getReg())
    print(myCar.getMake())
    print(myCar.getMilage())
    print(myCar.getDoi())

if __name__ == "__main__":
    main()