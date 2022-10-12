import math

def isPrime(x):
    if x%2 == 0 and x>2: return False
    for i in range(3, int(x**0.5)+1, 2):
        if x%i == 0: return False
    else: return True

def main():
    x = 13195
    factors = []
    while x != 1:
        for i in [2] + list(range(3, x, 2)):
            while x%i == 0:
                factors.append(i)
                x = x/i
    print(factors)

if __name__ == "__main__":
    main()
