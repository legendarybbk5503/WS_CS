import math

def main():
    sum = 0
    x = str(math.factorial(100))
    for i in x:
        sum += int(i)
    print(sum)

if __name__ == "__main__":
    main()