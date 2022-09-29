import math
import decimal

class Functions():
    def __init__(self):
        self.__phi__ = (1+5**0.5)/2
    
    def isPrime(self, x):
        sqrt = int(x**0.5)+1
        i = 3
        if x%2 == 0 and x > 2: return False
        elif x not in [2, 3]:
            while i < sqrt:
                if x%i == 0: return False
                else: i += 2
        return True
    
    def primeFactors(self, x):
        factors = []
        while x != 1:
            if self.isPrime(x):
                factors.append(x)
                x = 1
            else:
                for i in [2, 3] + list(range(3, x, 2)):
                    while x%i == 0:
                        if self.isPrime(i):
                            factors.append(i)
                            x /= i
        return factors
    
    def countFactors(self, x):
        count = 1
        factors = self.primeFactors(x)
        d = {factor:factors.count(factor) for factor in factors}
        for i in d.values(): count *= i+1
        return count
    
    def fibonacci(self, n):
        decimal.getcontext().prec = 100
        n = decimal.Decimal(n)
        self.__phi__ = decimal.Decimal(self.__phi__)
        a = decimal.Decimal(self.__phi__**n)
        b = decimal.Decimal((self.__phi__*-1)**(-1*n))
        x = int((a - b) / decimal.Decimal(5**0.5))
        return x


def main():
    pass

if __name__ == "__main__":
    main()