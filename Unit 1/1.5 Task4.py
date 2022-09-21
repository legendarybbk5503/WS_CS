def clear(row, column):
    park = []
    for i in range(row):
        temp = []
        for j in range(column):
            temp.append("empty")
        park.append(temp)
    print("Cleared")
    return park

def parking():
    reg = input("Enter the registration no: ")
    while True:
        row = int(input("Enter row no: "))
        column = int(input("Enter column no: "))
        if park[row][column] == "empty":
            park[row][column] = reg
            print("Parked")
            break
        else:
            print("This space isn't available")
            print("Please re-enter another one")

def remove():
    reg = input("Enter the registration no: ")
    for row in range(len(park)):
        try:
            column = park[row].index(reg)
        except: continue
        else: break
    park[row][column] = "empty"
    print("Removed")

def display():
    for i in range(len(park)):
        output = ""
        for j in range(len(park[i])):
            x = park[i][j]
            while len(x) < 9: x += " "
            output += x
        print(output)

def exit():
    print("Thank you for using")

def main():
    row = 20
    column = 25 
    global park
    park = clear(row, column)
    while True:
        option = int(input("Enter number of option: "))
        if option == 1: clear(row, column)
        elif option == 2: parking()
        elif option == 3: remove()
        elif option == 4: display()
        elif option == 5:
            exit()
            break

main()