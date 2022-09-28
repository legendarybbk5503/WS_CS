def isPrime(x):
    if x%2 == 0 and x>2: return False
    for i in range(3, int(x**0.5)+1, 2):
        if x%i == 0: return False
    return True

def main():
    x = 2+3+5+7
    for i in range(1, 200000):
        print(i)
        for j in (1, 3, 7, 9):
            if isPrime(i*10+j): x += i*10+j
    print(x)

if __name__ == "__main__":
    main()