class c():
    def multiple(table, startnum, endnum, pupilName):
        print(f"Hi, {pupilName} ... here is your times table")
        for i in range(startnum, endnum+1):
            print(f"{table} x {i} = {table*i}")

def main():
    print("What is your name?")
    pupilName = input()
    print("Enter times table, start number and end number")
    table = int(input())
    startnum = int(input())
    endnum = int(input())
    c().multiple(table, startnum, endnum, pupilName)

if __name__ == "__main__":
    main()
