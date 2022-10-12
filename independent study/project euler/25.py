from eulermath import Functions as f

def main():
    i = 1
    while True:
        if f().fibonacci(i) // 10**999 > 0:
            print(i)
            break
        i += 1

if __name__ == "__main__":
    main()