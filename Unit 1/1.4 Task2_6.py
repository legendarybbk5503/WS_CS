def reset(x, y): #size of the car park in row, column
    global park
    park = []
    for i in range(x):
        temp = []
        for j in range(y):
            temp.append("empty")
        park.append(temp)

def parksACar():
    reg = input("Enter the registration number of a car: ")
    while True:
        _input = input("Enter the grid reference (row, column): ")
        row = int(_input[:_input.find(",")]) - 1
        column = int(_input[_input.find(",")+1:]) - 1
        if row > len(park) or column > len(park[0]):
            print("Entry is invalid")
        elif park[row][column] != "empty":
            print("That space is taken")
        else:
            park[row][column] = reg
            output()
            break

def output():
    for i in range(len(park)):
        x = ""
        for j in range(len(park[0])):
            space = ""
            for _ in range(10-len(park[i][j])):
                space += " "
            x += park[i][j] + space
        print(x)

def main():
    reset(10, 6)
    while True:
        parksACar()

main()
