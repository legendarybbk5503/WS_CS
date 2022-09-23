class Marks():

    def __init__(self, __FileName=None):
        self.__FileName = __FileName


    def InputNew(self):
        self.__FileName = input("Enter a filename for the new file: ") + ".txt"
        try: 
            with open(self.__FileName, "x") as f: f.write("{}")
        except: print("The file exists, will continue with this file")
        self.InputAppend()

    def InputAppend(self):
        while True:
            name = input("Enter student's name: ")
            if not name: break
            marks = int(input("Enter student's marks: "))
            with open(self.__FileName, "r") as f:
                x = eval(f.read())
                x.update({name: marks})
            with open(self.__FileName, "w") as f: f.write(str(x))
            print("Press enter if you wanna quit")

    def Average(self):
        with open(self.__FileName, "r") as f: x = eval(f.read())
        marks = [i for i in list(x.values())]
        print(f"Average marks: {sum(marks)/len(marks)}")

    def Display(self):
        with open(self.__FileName, "r") as f: x = eval(f.read())
        for i in range(len(x)):
            print(f"{list(x.items())[i][0]}: {list(x.items())[i][1]}")

def main():
    print("1. Input data and save to new file")
    print("2. Input data and append to existing file")
    print("3. Calculate and display average mark")
    print("4: Display data")
    print("5: Quit")
    while True:
        choice = int(input("Choice: "))
        if choice == 1: c = Marks()
        elif choice in range(2, 5): c = Marks(input("Enter file name: ") + ".txt")
        elif choice == 5 or choice not in range(1, 5): break
        choices = ["c.InputNew()", "c.InputAppend()", "c.Average()", "c.Display()"]
        eval(choices[choice-1])


if __name__ == "__main__":
    main()