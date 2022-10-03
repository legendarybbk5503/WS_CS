def main():
    sum = 0
    for i in range(1, 1001):
        sum += i**i % (10**10)
    print(sum%(10**10))

if __name__ == "__main__":
    main()