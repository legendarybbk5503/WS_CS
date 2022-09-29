def main():
    x = 0
    for i in range(990, 0, -11):
        for j in range(999, 0, -1):
            if i*j > x and str(i*j) == str(i*j)[::-1]:
                x = i*j
        print(x)

if __name__ == "__main__":
    main()