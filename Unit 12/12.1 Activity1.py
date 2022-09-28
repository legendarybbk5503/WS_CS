import math 

class Circle():

    def __init__(self, radius = 0):
        if radius <= 0: self.__radius__ = 0
        else: self.__radius__ = radius
    
    def getRadius(self):
        return f"radius is {self.__radius__}"
    
    def setRadius(self, radius):
        self.__radius__ = radius
        return f"radius is now {self.__radius__}"
    
    def calcPerimeter(self):
        return f"Perimeter is {math.pi*2*self.__radius__}"
    
    def calcArea(self):
        return f"Area is {math.pi*(self.__radius__**2)}"

    def printCalculations(self):
        return self.calcPerimeter(), self.calcArea()

def main():
    c = Circle(-1)
    print(c.printCalculations())
    c.setRadius(1)
    print(c.printCalculations())
    ee = Circle(2.5)
    print(ee.printCalculations())

if __name__ == "__main__":
    main()