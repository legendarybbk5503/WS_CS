def findwithindex(i):
    print(f"Name: {name[i-1]}")

def search(max):
    result = []

    for i in range(0, len(name)):
        if max.lower() in name[i].lower():
            result.append(name[i])

    if len(result) > 0:
        output = f"The names are {result[0]}"
        for i in range(1, len(result)):
            output += (f", {result[i]}")
        print(output)
    else:
        print("The name doesn't exist")

#-----------------------------------------------------------------------------------------------------------------

name = ["Tom", "Sam", "Jerry", "Bobby"]
isContinue = ""

while isContinue == "":
    choice = int(input("Type 1 for getting a name with index\nType 2 for searching a name containing an element\n"))
    if choice == 1:
        i = int(input("Index: "))
        findwithindex(i)
    elif choice == 2:
        max = input("element contained: ")
        search(max)
    isContinue = input("Press Enter to continue, type others to exit")