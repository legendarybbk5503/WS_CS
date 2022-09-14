school = ["AAAA", "BBBB", "CCCC", "DDDD"]
medal = [0, 0, 0, 0]

def newResult():
    while True:
        choice = int(input("Enter corresponding number for school: "))
        if choice == -1: break
        elif choice in range(1, len(school)+1):
            medal[choice-1] += 1
        else: print("Invalid school number")

def output():
    for i in range(len(school)):
        print(f"School number {i+1}   School name {school[i]}   Number of medals {medal[i]}")

def main():
    print("1: AAAA")
    print("2: BBBB")
    print("3: CCCC")
    print("4: DDDD")
    newResult()
    output()

main()