school = ["AAAA", "BBBB", "CCCC", "DDDD"]
medal = [0, 0, 0, 0]

def newResult():
    while True:
        choice = int(input("Enter corresponding number for school: "))
        if choice == -1: break
        medal[choice-1] += 1

def output():
    for i in range(len(school)):
        print(f"School number {i}   School name {school[i]}   Number of medals {medal[i]}")

def main():
    print("1: AAAA")
    print("2: BBBB")
    print("3: CCCC")
    print("4: DDDD")
    newResult()
    output()

main()