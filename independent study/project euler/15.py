import math

def main():
    print(math.comb(40, 20))

if __name__ == "__main__":
    main()

#left = 0, down = 1
#1*1 = [10, 01] -> 2 = 2C1
#2*2 = [0011, 0110, 0101, 1001, 1010, 1100] -> 6 = 4C2
#...
#20*20 = 40C20