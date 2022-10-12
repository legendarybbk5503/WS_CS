def main():
    x = str(2**1000)
    sum = 0
    for i in range(len(x)):
        sum += int(x[i])
    print(sum)


if __name__ == "__main__":
    main()
