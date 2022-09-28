class C():
    def __init__(self):
        self.__found__ = {}

    def collatz(self, num):
        x = num
        count = 1
        while x != 1:
            if x in self.__found__:
                count = count + self.__found__[x] -1
                break
            elif x%2 == 0: x = x/2
            else: x = 3*x+1
            count += 1
        self.__found__.update([(num, count)])
        return count
    
    def largest(self):
        return max(self.__found__, key = self.__found__.get)

def main():
    c = C()
    for i in range(1, 1000000):
        print(i)
        c.collatz(i)
    print(c.largest())

if __name__ == "__main__":
    main()