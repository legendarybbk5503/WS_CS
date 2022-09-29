def isPrime(x):
    sqrt = int(x**0.5)+1
    i = 3
    if x%2 == 0 and x > 2: return False
    elif x not in [2, 3]:
        while i < sqrt:
            if x%i == 0: return False
            else: i += 2
    return True

def primeFactors(x):
    factors = []
    while x != 1:
        if isPrime(x):
            factors.append(x)
            x = 1
        else:
            for i in [2, 3] + list(range(3, x, 2)):
                while x%i == 0:
                    if isPrime(i):
                        factors.append(i)
                        x /= i
    return factors

def countFactors(x):
    count = 1
    factors = primeFactors(x)
    d = {factor:factors.count(factor) for factor in factors}
    for i in d.values(): count *= i+1
    return count

def main(): #formula for triangle number: (n)(n+1)/2
    count, n = 1, 2
    while True:
        factors = primeFactors(n) + primeFactors(n+1)
        d = {factor:factors.count(factor) for factor in factors}
        count = d[2]
        d.pop(2)
        for i in d.values():
            if count == 1: count *= i
            else: count *= i+1
        if count > 500: break
        n += 1  
    print((n)*(n+1)//2)


if __name__ == "__main__":
    main()