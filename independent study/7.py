def isPrime(x):
    if x%2 == 0 and x>2: return False
    for i in range(3, int(x**0.5)+1, 2):
        if x%i == 0: return False
    return True

def main():
    prime, i = [2], 3
    while len(prime) <= 10000:
        if isPrime(i): prime.append(i)
        i += 2
    print(prime[-1])

if __name__ == "__main__":
    main()